import { test, expect } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

test.describe("SuiteDash preview governance checks", () => {
  test("renders key launch-truth messaging", async ({ page }) => {
    await page.goto("/index.html");

    await expect(
      page.getByRole("heading", {
        name: "The 90-minute operator path through SuiteDash."
      })
    ).toBeVisible();
    await expect(
      page.getByRole("heading", {
        name: "The preview is live. Production still needs the external switches flipped."
      })
    ).toBeVisible();
    await expect(page.locator('meta[name="robots"]')).toHaveAttribute(
      "content",
      /noindex/
    );
  });

  test("supports keyboard navigation and skip-link access", async ({ page }) => {
    await page.goto("/index.html");
    await page.keyboard.press("Tab");

    const skipLink = page.getByRole("link", { name: "Skip to content" });
    await expect(skipLink).toBeFocused();
    await skipLink.press("Enter");
    await expect(page.locator("#main-content")).toBeInViewport();
  });

  test("has no serious or critical axe violations", async ({ page }) => {
    await page.goto("/index.html");

    const results = await new AxeBuilder({ page }).analyze();
    const blocking = results.violations.filter((violation) =>
      ["serious", "critical"].includes(violation.impact)
    );

    expect(blocking).toEqual([]);
  });

  test("holds mobile layout without horizontal overflow", async ({ page }) => {
    await page.goto("/index.html");

    const overflow = await page.evaluate(() => {
      const root = document.documentElement;
      return root.scrollWidth - root.clientWidth;
    });

    expect(overflow).toBeLessThanOrEqual(1);
    await expect(
      page.getByRole("link", { name: "Review launch status" })
    ).toBeVisible();
  });
});

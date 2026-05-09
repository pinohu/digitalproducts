const makeFrame = (title, frameStyles = "") => `
  <div style="background:#f4efe4;padding:24px;min-height:100vh;">
    <h1 style="font:700 20px/1.2 Arial,sans-serif;margin:0 0 16px;">${title}</h1>
    <iframe
      title="${title}"
      src="/suitedash-preview/index.html"
      style="width:100%;height:2200px;border:1px solid rgba(19,34,56,0.12);border-radius:18px;background:white;${frameStyles}"
    ></iframe>
  </div>
`;

export default {
  title: "Governance/SuiteDash Preview"
};

export const DesktopReview = {
  render: () => makeFrame("Desktop review")
};

export const MobileReview = {
  render: () =>
    makeFrame(
      "Mobile review",
      "max-width:430px;display:block;margin:0 auto;height:1800px;"
    )
};

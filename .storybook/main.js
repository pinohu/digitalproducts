export default {
  framework: {
    name: "@storybook/html-vite",
    options: {}
  },
  stories: ["../governance/storyboard/**/*.stories.js"],
  addons: ["@storybook/addon-essentials", "@storybook/addon-a11y"],
  staticDirs: [
    {
      from: "../08-platforms/vercel-sites/suitedash-good-parts-preview",
      to: "/suitedash-preview"
    }
  ]
};

## Summary

- What changed?
- Why now?
- Which issue or operator lane does this advance?

## Governance checklist

- [ ] I updated repo truth docs if product status, launch status, or operator capability changed.
- [ ] I attached or linked evidence for the quality checks that matter here.
- [ ] I recorded any remaining blockers truthfully instead of implying production is live.
- [ ] I added a changeset if this materially changes release notes or governance expectations.

## Quality evidence

- [ ] `npm run test:e2e`
- [ ] `npm run test:a11y`
- [ ] `npm run test:lighthouse`
- [ ] Storybook review completed for affected surfaces

## Accessibility and UX

- [ ] Keyboard navigation checked
- [ ] Focus states checked
- [ ] Mobile layout checked
- [ ] Copy, hierarchy, and CTA clarity checked

## Release safety

- [ ] No live write, send, billing, or destructive action was enabled without explicit authorization
- [ ] If release-state changed, `governance/release-state.json` still matches reality

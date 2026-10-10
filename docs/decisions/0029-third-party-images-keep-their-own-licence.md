# 0029. A third-party image keeps its own licence

- **Status:** Accepted
- **Decided:** 2026-10-10 · **Recorded:** 2026-10-10 · Claude Opus 5.5
- **Affects:** images under `docs/essays/images/`; the README's License section; `plugin.json`

## Context

[0014](0014-license-cc-by-4-0.md) licenses "every file" outside `evals/` under CC BY 4.0, and
rejected CC BY-SA because ShareAlike draws licence review and scanners stop on it. The repo held
no images then.

Hampton asked for a photograph of W. Edwards Deming in the TQM essay, under a permissible licence.
The search found four candidates, all on Wikimedia Commons. The two that are public domain are
393×274 and 277×207 pixels. The two that are sharp are CC BY-SA 4.0. Hampton chose one of those
on 2026-10-10: "the neave photo is the only one that's high quality." It was added in
[#151](https://github.com/cobarx/build-skills/pull/151).

The owner cannot relicense someone else's photograph, so the image cannot fall under 0014.

## Options

- **Only images that are public domain or CC BY.** Keeps 0014 whole. For this essay it means a
  thumbnail or no photo.
- **Link to the image on Commons without holding a copy.** No BY-SA file enters the repo. The
  essay then breaks when the remote file moves or is deleted. Not put to Hampton before he chose.
- **Hold a copy under its own licence, credited where it appears.**

## Decision

An essay may carry a third-party image under that image's own licence, ShareAlike included. The
copy lives in `docs/essays/images/`. A footnote in the essay gives its title, author, source, and
licence, and says whether it was changed. The README's License section names the exception.

This amends 0014's scope, not its choice: the owner's text stays CC BY 4.0.

## Consequences

- **The essay stays CC BY.** Creative Commons allows licensed material in a collection, and "You
  may choose a license for the collection, however this does not change the license applicable to
  the original material."[^cc] The first image is a byte-identical copy, so nothing was adapted.
- **A changed image is an adaptation.** A crop or an edit of a BY-SA image must itself be offered
  under BY-SA, and its footnote must say what changed.
- **The plugin ships the image.** The marketplace entry's `source` is `./`, so an install carries
  `docs/`. A scanner or a blanket copyleft policy, the cost 0014 named, can now find one BY-SA
  file. It is an image beside an essay, and no skill depends on it.
- **`plugin.json` says `CC-BY-4.0 AND Apache-2.0`.** Whether it should also name `CC-BY-SA-4.0`,
  or the plugin should stop shipping `docs/`, is open.
- **The licence is as good as the uploader's claim.** The first image was uploaded as "own work"
  in 2025 with no verification on Commons of who took it. If the claim is withdrawn or the file is
  deleted there, the copy here comes out.

[^cc]: Creative Commons, "Frequently Asked Questions", "If I create a collection that includes a
    work offered under a CC license, which license(s) may I choose for the collection?",
    <https://creativecommons.org/faq/#if-i-create-a-collection-that-includes-a-work-offered-under-a-cc-license-which-licenses-may-i-choose-for-the-collection>,
    retrieved 2026-10-10.

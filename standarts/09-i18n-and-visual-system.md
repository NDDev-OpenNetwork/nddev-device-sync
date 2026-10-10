# Internationalization and visual system

## Language

Code, API paths, event names, logs, schemas, database identifiers and release
metadata use English. The UI ships with `en` and `ru` locales from the first
user-facing release. English is the source locale and Russian translations are
validated for missing keys, placeholders, plural forms and layout overflow.

The canonical message catalog uses ICU-compatible ARB resources so Flutter's
generated localization workflow and other clients can share message IDs and
formatting rules. Locale-sensitive dates, numbers, units and plural forms are
formatted by the platform localization libraries.

## NDDev OpenNetwork visual direction

Use the existing NDDev platform's OpenNetwork direction: yellow/gold accents,
neutral dark/light surfaces, IBM Plex Sans and its control geometry and states.
[ADR 0004](decisions/0004-opennetwork-visual-source.md) corrects the earlier
independently styled NDS palette.

The public `nddev-opennetwork-design-system` repository owns the versioned
OpenNetwork token and native UI-kit projection. New screens consume its colors,
typography, spacing, radii, focus and interaction states; they do not introduce
local one-off styling. Preserve the authentic NDDev mark and the OpenNetwork
direction colors in application and launcher assets. Reusable visual sources
and redistributable fonts carry provenance and licenses; private site content,
configuration and screenshots stay outside public packages.

Every important state has text and an accessible representation. Native controls
retain keyboard, focus, disabled/error semantics and text scaling. Theme-specific
contrast corrections remain authoritative; decoration never obscures status.

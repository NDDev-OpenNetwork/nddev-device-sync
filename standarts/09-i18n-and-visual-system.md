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

## NDDev visual direction

Generated images, illustrations and empty states combine three references:

- NDDev's architecture-first, systems-oriented language from `nddev.it.com`;
- NDDev.AI's agent and intelligence direction;
- a restrained space/observatory motif for devices, telemetry and network
  relationships.

The color palette, typography scale, spacing, radii, shadows and icon rules
come from the NDDev Platform design system. New screens consume design tokens;
they do not introduce local one-off colors or typography. The visual language
uses dark observatory surfaces, clear status colors, structured grids and
controlled cosmic accents. Decorative space imagery must never reduce
contrast, obscure status, or compete with operational information.

Generated assets are original and fit the system's tokens. Logos, screenshots
and protected site assets are not copied into the application. Every important
state also has a text and accessible representation.


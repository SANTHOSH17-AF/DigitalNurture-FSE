"""
Step 35 - rank the 6 locator strategies from most to least preferred for
maintainable automation, with justification.
"""

# Ranking (most to least preferred):
#
# 1. ID              - fastest, guaranteed unique per spec, very readable.
# 2. CSS Selector     - fast, flexible, easy to read; works for attribute and
#                        structural matches without XPath's verbosity.
# 3. NAME             - usually stable and unique within a form, but not
#                        guaranteed unique across the whole page.
# 4. Relative XPath   - powerful (can match on text, traverse parent/sibling
#                        axes) but more verbose and slightly slower than CSS;
#                        use it only when CSS genuinely can't express the
#                        condition (e.g. matching by visible text).
# 5. CLASS_NAME/TAG_NAME - rarely unique on their own (many elements share a
#                        class or tag), so brittle as a sole locator - best
#                        combined with another attribute.
# 6. Absolute XPath   - least preferred: encodes the exact DOM structure from
#                        the document root, so it breaks the instant any
#                        ancestor element is added, removed, or reordered -
#                        the most fragile option by far.
#
# Justification: uniqueness and stability matter most for long-term
# maintainability. ID and CSS selectors are both fast to evaluate and
# resistant to unrelated markup changes elsewhere on the page, while absolute
# XPath is tightly coupled to the entire page's structure and breaks with
# almost any layout change - making it the worst choice for a durable suite.

print("See ranking and justification in the comment block above.")

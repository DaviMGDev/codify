.PHONY: check-duplicates

check-duplicates:
	@diff -q LANGUAGE.md skills/codify/references/LANGUAGE.md || \
		(echo "❌ ERROR: LANGUAGE.md differs from skills/codify/references/LANGUAGE.md"; \
		 echo "   These files must be identical per ADR 002 (docs/adr/002-duplicate-files-in-skill-bundle.md)."; \
		 echo "   If this divergence is intentional, include [skip-drift] in your commit message."; \
		 exit 1)
	@diff -q example.md skills/codify/assets/examples/example.md || \
		(echo "❌ ERROR: example.md differs from skills/codify/assets/examples/example.md"; \
		 echo "   These files must be identical per ADR 002 (docs/adr/002-duplicate-files-in-skill-bundle.md)."; \
		 echo "   If this divergence is intentional, include [skip-drift] in your commit message."; \
		 exit 1)
	@echo "✅ All duplicate files in sync."

SKILL_DIR := linkedin-post-generator
DIST_DIR  := dist
ZIP_FILE  := $(DIST_DIR)/$(SKILL_DIR).zip

.PHONY: validate build clean

validate:
	python3 scripts/validate.py

build: validate
	mkdir -p $(DIST_DIR)
	zip -r $(ZIP_FILE) $(SKILL_DIR) \
		--exclude "*.DS_Store" \
		--exclude "*/._*" \
		--exclude "*/__MACOSX/*" \
		--exclude "__MACOSX/*"
	@echo ""
	@echo "Build completato: $(ZIP_FILE)"
	@unzip -l $(ZIP_FILE)

clean:
	rm -rf $(DIST_DIR)

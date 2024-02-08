# SPDX-FileCopyrightText: 2024 Shell Global Solutions International B.V. All Rights Reserved.
#
# SPDX-License-Identifier: Apache-2.0

import re

with open("pyproject.toml", "r") as file:
    version_content = file.read()
# Match regex for <version="0.0.0a",> pattern
old_semantic_version = re.findall(r'version = "(\d+\.\d+\.[a-zA-Z0-9]+)"', version_content)
major_version, minor_version, patch_version = old_semantic_version[0].split(".")
patch_version = int(re.findall(r"\d+", patch_version)[0])
new_semantic_version = f"{major_version}.{minor_version}.{patch_version + 1}"
regex_bumped_patch_version = f"\g<1>{new_semantic_version}"
# Match regex for <version = "0.0.0a"> pattern
bumped_version_content = re.sub(r'(version = ")\d+\.\d+\.[a-zA-Z0-9]+', regex_bumped_patch_version, version_content)
with open("pyproject.toml", "w") as file:
    file.write(bumped_version_content)
print(new_semantic_version)  # Print is required for release in GitHub action

## Starsector Mod Template

This is just a personal mod template for my own use.

# Setup
This is using the VSCode extension "Java Project Manager"
Once created from template, it should look something like this once cloned

Something like:
```
starsector
⨽mods
  ⨽Repo Name (Mod name)
    ⊢.git
    ⨽.vscode
      ⨽settings.json
    ⨽lib
      ⨽standard libs from Starsector
    ⊢jars (Will appear on first build)
    ⨽src
      ⨽org
        ⨽tuvox
          ⨽ModPlugin.jar
    ⊢README.md
    ⨽init.py
```

`init.py` should be run after you clone the repository, it sets the Mod Name to the Parent folder name and then tweaks the `mod_info.json` with that information.

`release.py` will package up the necessary files for release after asking for the new version number.

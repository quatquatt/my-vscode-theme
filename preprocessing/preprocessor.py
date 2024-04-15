import json
import os

# Define color variables
red = "#ff2626"
orange = "#ff9a47"
green = "#2fd22d"
light_blue = "#4dfcff"
dark_blue = "#1d9dd0"
purple = "#d17aff"
dark_purple = "#d587ff"
black = "#000000"
dark_gray = "#111111"
gray = "#333333"
white = "#ffffff"

# Define the structure of the JSON file
data = {
    "name": "My VSCode Theme",
    "type": "dark",
    "semanticHighlighting": True,
    "colors": {
        "editor.background": black,

		"activityBar.background": black,
		"activityBar.foreground": dark_purple,

		"activityBarBadge.background": "#4D78CC",
		"activityBarBadge.foreground": "#f8f8f8",
        
		"sideBar.background": black,
		"sideBar.foreground": "#cccccc",
		"sideBarTitle.foreground": white,
		"sideBarSectionHeader.background": "#1F2330",

		"editor.findMatchBackground": "#00000000",
		"editor.findMatchHighlightBackground": "#00000000",
		"editor.wordHighlightBackground": gray,
		"editor.wordHighlightStrongBackground": gray,
		"editor.lineHighlightBackground": dark_gray,
		"editor.selectionBackground": "#484e5b",
		"editor.selectionHighlightBackground": "#00000000",

		"textLink.foreground": light_blue,
		"textLink.activeForeground": "#00ff00",

		"button.background": "#348200",
		"button.foreground": white,

		"statusBar.background": black,
		"statusBar.foreground": white,
		"statusBarItem.hoverBackground": "#2c313a",
		"statusBar.noFolderBackground": black,
		"statusBar.debuggingBackground": black,

		"titleBar.activeBackground": black,
		"titleBar.activeForeground": white,
		"titleBar.inactiveBackground": black,
		"titleBar.inactiveForeground": "#6B717D",

		"dropdown.background": black,
		"dropdown.border": "#181A1F",

		"list.inactiveSelectionBackground": dark_gray,
		"list.activeSelectionBackground": dark_gray,
		"list.inactiveSelectionForeground": "#50fa7b",
		"list.activeSelectionForeground": "#50fa7b",
		"list.focusBackground": "#383E4A",
		"list.hoverBackground": "#292d35",
		"list.highlightForeground": "#C5C5C5",
		"list.focusOutline": black,

		"listFilterWidget.background": black,
		"listFilterWidget.outline": "#4D78CC",
		"listFilterWidget.noMatchesOutline": "#c24038",

		"scrollbarSlider.background": "#4E566680",
		"scrollbarSlider.activeBackground": "#747D9180",
		"scrollbarSlider.hoverBackground": "#5A637580",

		"editorCursor.foreground": white,
		"editorError.foreground": "#c24038",
		"editorMarkerNavigation.background": "#21252b",
		"editorRuler.foreground": "#AAB1C026",
		"editorGroup.border": "#181A1F",
		"editorGroupHeader.tabsBackground": black,
		"editorIndentGuide.background1": "#3B4048",
		"editorLineNumber.foreground": "#495162",
		"editorWhitespace.foreground": "#3B4048",
		"editorHoverWidget.background": black,
		"editorHoverWidget.border": "#181A1F",
		"editorSuggestWidget.background": black,
		"editorSuggestWidget.border": "#181A1F",
		"editorSuggestWidget.selectedBackground": "#2c313a",
		"editorWidget.background": "#21252B",

		"badge.background": "#282c34",
		"debugToolBar.background": black,
		"diffEditor.insertedTextBackground": "#00809B33",
		"input.background": "#1d1f23",
		"peekViewEditor.matchHighlightBackground": "#29244b",

		"tab.activeBackground": black,
		"tab.border": black,
		"tab.inactiveBackground": black,

		"terminal.ansiBlack": "#2D3139",
		"terminal.ansiBlue": "#2e8ccf",
		"terminal.ansiGreen": "#98c379ff",
		"terminal.foreground": "#C8C8C8",
		"terminal.ansiYellow": "#B4881D",
    },
    "tokenColors": [
        {
            "scope": "storage.type.primitive.java",
            "settings": {
                "foreground": green
            }
        }
    ],
    "semanticTokenColors": {
		"variable.declaration": orange,
		"parameter.declaration": {
			"foreground": orange,
			"fontStyle": "italic"
		},

		"modifier": dark_blue,
		"keyword": dark_blue,

		"class": green,
		"type": green,

		"method": light_blue,
		"function": light_blue,

		"comment": purple,

		"string": "#f5ff80",

		"number": red,
		
		"operator": white,
		"property": white,
		"variable": white,
		"parameter": {
			"foreground": white,
			"fontStyle": "italic"
		}
	}
}

output_path = os.path.join('.', 'theming', 'my-vscode-theme.json')

# Write the JSON file to the correct directory
with open(output_path, 'w') as f:
    json.dump(data, f)
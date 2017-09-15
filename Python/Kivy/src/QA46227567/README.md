# Kivy self.ids method

This example illustrates how to access widgets defined inside Kv language in your Python code using self.ids method.

## Snippet
        self.ids[button_pressed].background_normal = kivy_logo

## Note
Although the self.ids method is very concise, it is generally regarded as 'best practice' to use the ObjectProperty. This
creates a direct reference, provides faster access and is more explicit.

## Links
[Problems referencing items in a kv with kivy](https://stackoverflow.com/questions/46227567/problems-referencing-items-in-a-kv-with-kivy)

## Images
![App Startup](https://github.com/ikolim/StackExchange/blob/master/Python/Kivy/images/QA46227567/Img01-Startup.png "App Startup")
![Screen1](https://github.com/ikolim/StackExchange/blob/master/Python/Kivy/images/QA46227567/Img02-PlayerName-Entered.png "Player Name Entered")
![Screen2](https://github.com/ikolim/StackExchange/blob/master/Python/Kivy/images/QA46227567/Img03-Screen2-Displayed.png "Game Board Displayed")
![Button](https://github.com/ikolim/StackExchange/blob/master/Python/Kivy/images/QA46227567/Img04-TopLeft-Button-Pressed.png "TopLeft Button Pressed & Background Image Changed")

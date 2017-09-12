# Kivy Drop-Down List

This example illustrates how to create drop-down list.

## Links
https://stackoverflow.com/questions/46060693/referenceerror-weakly-referenced-object-no-longer-exists-kivy-dropdown

## Problem Explanations for StackOverflow 46060693
### In child widget, CustomDropDown

#### With on_parent: self.dismiss()

When you clicked on the main button, **Menu name** sometimes it gives an error, **_ReferenceError: weakly-referenced object no longer
exists_**. If there is no **_ReferenceError_**, the drop-down list flash (appear and quickly disappear). The reason is that the DropDown
was dismissed.

#### Without on_parent: self.dismiss()

It will display the CustomDropDown list at app startup. When the main button, **Menu name** is clicked, the drop-down list that 
appeared at startup disappeared but it displayed a drop-down list twice as long i.e. submenu items repeated twice.

### Note

Drop-Down List is similar to Popup. They are special widget. Don't try to add it as a child to any other widget. If you do, 
they will be handled like an ordinary widget and won't be created hidden in the background.

## Images
![App Startup](https://github.com/ikolim/StackExchange/blob/master/Python/Kivy/images/QA46060693/Img01-Startup.png "App Startup")
![DropDown List](https://github.com/ikolim/StackExchange/blob/master/Python/Kivy/images/QA46060693/Img02-DropDownList.png "Clicked Menu name")
![First Item](https://github.com/ikolim/StackExchange/blob/master/Python/Kivy/images/QA46060693/Img03-Selected-FirstItem.png "First Item Selected")
![DropDown List 1](https://github.com/ikolim/StackExchange/blob/master/Python/Kivy/images/QA46060693/Img04-DropDownList.png "Clicked Menu name")
![Second Item](https://github.com/ikolim/StackExchange/blob/master/Python/Kivy/images/QA46060693/Img05-Selected-SecondItem.png "Second Item Selected")
![DropDown List 2](https://github.com/ikolim/StackExchange/blob/master/Python/Kivy/images/QA46060693/Img06-DropDownList.png "Clicked Menu name")
![Third Item](https://github.com/ikolim/StackExchange/blob/master/Python/Kivy/images/QA46060693/Img07-Selected-ThirdItem.png "Third Item Selected")
![DropDown List 3](https://github.com/ikolim/StackExchange/blob/master/Python/Kivy/images/QA46060693/Img08-DropDownList.png "Clicked Menu name")
 

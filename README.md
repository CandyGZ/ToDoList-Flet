# Technical Document - Flet Task Management App
#Overview#
This technical document provides an overview of the Flet Task Management App and describes the libraries and technologies used in its development. The app is designed for managing a very simple TO-Do list for a kid, featuring a user-friendly interface.

## Technologies Used
The Flet Task Management App is built using the following technologies and libraries:

## Flet
Flet is a Python library for creating cross-platform user interfaces. It simplifies the development of graphical user interfaces (GUI) for desktop and mobile applications.

## Custom Checkbox Library
The Custom Checkbox Library is a custom component that extends the functionality of Flet to create interactive and customizable checkboxes for tasks.

## Python
Python is the primary programming language used to develop the Flet Task Management App. It is a versatile language with extensive libraries and frameworks, making it suitable for both rapid development and complex applications.


    ```python
    app(target=main, assets_dir="assets")

Main Function
The main function serves as the main logic for the application. It configures the app's theme, defines color constants, and creates the main user interface components.

Theme Configuration
The app's theme mode is set to "dark" for white text and icons.

    ```python
    page.theme_mode = "dark"

User Interface Components
The main user interface components include circular avatars, task lists, category displays, and buttons for task creation.

## Circular avatars
are created using Flet's Stack and Container controls. These avatars can contain user images and act as visual elements in the app.

## Task lists
are displayed as scrollable columns with custom checkboxes for task management. Sample tasks are populated within the list.

## Categories
are shown as horizontal rows, and categories such as "School," "Family," and "Friends" are displayed.

## Buttons
for creating tasks are represented by a floating action button (FAB) with an "Add" icon.

## Page Routing
The app employs page routing to transition between different views, such as the main view and the task creation view. Route change handling is implemented to update the displayed view when the route changes.

  page.go(page.route)

## Conclusion
This Flet Task Management App is a basic Python application that utilizes the Flet framework for creating a visually appealing and interactive task management interface. The use of custom components, such as the custom checkbox library, enhances the user experience. By defining themes and handling page routing, the app provides an engaging user experience for managing tasks and categories and is still in development.

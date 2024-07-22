Release History
===============

0.0.7 (2024-07-22)
------------------

### New Features

- Added `SaveConsoleLog` Action to save the console logs encountered during a test.

### Dev Niceties

- Reorganized classes to have consistent method organization.


0.0.6 (2024-07-16)
------------------

### New Features

- Added `IsPresent` Resolution, which checks if an element, uh, is present.

### Improvements

- Addressed several issues with the Target class, such as them not appearing as Locators. We had to do some pretty spooky magicks back here, but don't worry; you'll get autocompletion and proper typing!
- Added wrapping around interacting with Playwright Locators to make the error messages a little more readable from a higher level.


0.0.5 (2024-05-22)
------------------

### Bug Fixes

- Fixed typing errors with `Enter.the_password`.
- Fixed typing errors with `Target`, or more specifically with `_Manipulation`, or even more specifically with specifying the types of the `args` and `kwargs` which are passed on to Playwright's API.


0.0.4 (2024-05-15)
------------------

### New Features

- Added several new Actions: `RefreshThePage`, `Scroll`, `Select`
- Added two new Questions: `BrowserURL`, `Element`
- Added a new Resolution: `IsVisible`
- Added several aliases for the existing Actions, Questions, and Resolutions.
- `Target` now also fully supports all Playwright locator methods.

### Bug fixes

- Enabled multiple Actors to be able to `exit` without breaking Playwright for each other.


0.0.3 (2024-02-21)
------------------

### New Features

- Added new Action: ``SaveScreenshot``
- Added new Question: ``Attribute``
- `Target` can now find things in iframes!

## Development Niceties

- ScreenPy: Playwright is now standardized with the other ScreenPy projects (thanks, @bandophahita)!


0.0.2 (2024-02-13)
------------------

### Improvements

- Made all the user-facing features of ScreenPy: Playwright importable from the root, like the other ScreenPy plugins.

### Development Niceties

- Added Poetry!
- Added ruff!
- It's nice!!!


0.0.1 (2022-09-18)
------------------

### Timeline

- Initial release!

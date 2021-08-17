# Zerodays Challenge

This is a simple React challenge, designed for newcomers to familiarize themselves with our usual development stack and workflow.

## 1. Project goals:
- Set up a new React project. We'll use functional components.
- Install a few frameworks we usually use:
    - [nextjs](https://nextjs.org/) - to be used mostly for routing, links, and images.
    - [tailwindcss](https://tailwindcss.com/docs/guides/create-react-app) - UI is to be built with tailwindcss components. Note that tailwindcss is free, while tailwindui is not. We use tailwindcss for its utilities (flex, grid).
    - [axios](https://www.npmjs.com/package/axios) - to be used for all API calls.
- Create 2 pages, further described below.
- Make some REST API calls. The API is available at [challenge.zerodays.dev/api/v1/](https://challenge.zerodays.dev/api/v1/).
- Show some sort of error message whenever an API request fails. 

## 2. Pages

#### `/`
The main page of your app. It should:
- Load a list of insanely cool animal images from `/photos` (the full URL is [https://challenge.zerodays.dev/api/v1/photos](https://challenge.zerodays.dev/api/v1/photos)). Do show a progress indicator while loading.
- Display the loaded images in a list/grid, depending on the screen size. Try to use tailwindcss utilities for responsiveness. Images are to be displayed using `Image` from `nextjs/image`.
- Each image must have:
    - Current like and dislike counts. This can be a progress bar like on YouTube or any other way you like it.
    - Like and dislike buttons. On press, execute a PATCH request to `/photos/:id/like` and `/photos/:id/dislike` respectively. While the request is in progress, show some sort of progress indicator. The API returns a new image object with updated like and dislike counts. Replace the old image data with the new one in order for your like to count!


#### `/404`
Page served for any other url, not present on the server. Doesn’t need to be anything special, just make a custom site instead of next’s default one.

## 3. Some quick notes before you start:
- This is not a time trial. Take your time and create something you are proud of.
- Don’t hesitate to ask for help of further explanation.
- Make sure the user interface is functional. This is not a design challenge, however usability is important.
- The website must be responsive.
- You can ignore localization.
- Other libraries are not forbidden. Need some additional icons or styles? Go for it! Just make sure you use grid and flex utilities from tailwind.
- Server source code is available in this repository in case you want to study it.

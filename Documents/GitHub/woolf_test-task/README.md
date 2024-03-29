## Preparing for work

1. Make sure that the LTS version of Node.js is installed on the computer.
   [Download and install](https://nodejs.org/en/) if necessary.
2. Install the project's basic dependencies using the `npm install` command.
3. Start the development mode, execute the `npm start` command.
4. Go to [http://localhost:3000](http://localhost:3000) in the browser. This
   page will automatically reload after saving the changes project files.

---

# Test task

Your task is to develop an application for a company offering camper van rental
services in Ukraine.

#### The application comprises three pages:

1. Home page featuring a general description of the company's services.
   Stylization and design at your discretion.
2. A catalog page showcasing campers of various configurations, allowing users
   to filter by location, equipment, and type.
3. A favorites page displaying ads that users have saved.

The application's layout should include a navigation section (design according
to your preferences) and a viewing area.

## Technical task

1. Based on the
   [layout](https://www.figma.com/file/fnMWH0eBB7NnoqdAiiKWsQ/Test?type=design&node-id=0-1&mode=design&t=Y12LBROdvbgZJBFC-0),
   create a card to announce the availability of camper rentals.
2. Display four ads on the initial catalog page, with the remaining ads
   appearing after clicking the 'Load More' button.
3. When you click on the 'heart' button on the ad card, it should be added to
   your list of favorites, and the color of the button should change.
4. Upon refreshing the page, the user's actions should persist. For example, if
   an ad is added to favorites, the 'favorite ad' state with the appropriate
   color should remain for the button.
5. When you click the heart button again, the ad should be removed from your
   list of favorites, and the color of the button should revert to its original
   state.
6. When you click the 'Show more' button, a modal window should open, displaying
   detailed information about the camper.
7. The modal window should close when clicking the 'cross' button, clicking on
   the backdrop, or pressing the Esc key.
8. The modal window should display information about the characteristics of the
   camper and reviews. The content shown should depend on the state of the
   active tab.
9. The modal window includes a reservation form for booking a camper, featuring
   fields for name, email, booking date, and optional comments. The name, email,
   and booking date fields are mandatory and must be validated for accuracy. If
   the entered data is invalid, the form will not be submitted. Upon successful
   completion of a valid form, the page will be updated.
10. The rental price should be entered as a single value (for example, 8000),
    and in the user interface, it should be displayed with a comma (e.g.,
    8,000.00).

To manage the list of advertisements, set up your personal backend for
development using the UI service provided by
[https://mockapi.io/](https://mockapi.io/). Create an 'adverts' resource and
define the ad object according to the description below.

### Advert

1. Create an advertisement in Mockapi with the following fields: \_id, name,
   price, rating, location, adults, children, engine, transmission, form,
   length, width, height, tank, consumption, description, details, gallery, and
   reviews (refer to the screenshot below). You can populate the collection
   using the [adverts.json](./assets/adverts.json) file.
2. You have the freedom to select the image of the camper yourself.
3. Ensure the database includes a minimum of 13 ads, each with distinct content
   (chosen at your discretion). Implement pagination, with each page displaying
   4 ads.

### Create routing using React Router

The application should include the following routes:

- "`/`" - Home page with a general description of services provided by the
  company.
- "`/catalog`" - Page containing a catalog of campers of various configurations.
- "`/favorites`" - Page with announcements (design at your discretion) that have
  been added to favorites by the user.

## Additional task

#### Implement filtering functionality:

1. If a location is entered into the text input, the user should be shown ads
   featuring campers located in that area.
2. Checkboxes for specific equipment should display ads featuring campers
   equipped with the selected items.
3. For radio buttons indicating types of campers, ads should be shown for
   campers corresponding to the selected type.

#### Define performance criteria for the project

- Ensure the layout is fixed, semantic, and valid. Verify that there are no
  errors in the browser console.
- Mandatory usage of Redux.
- Utilize the Axios library for queries.
- Develop the project in native JS using a bundler such as Vite, Parcel, etc.,
  or in React.
- Ensure interactivity aligns with the project's specifications.
- Format the code and include comments for clarity.
- Describe the repository in the [README.md](https://tiloid.com/) file.
- Deploy the project on GitHub Pages or Netlify.

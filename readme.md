# GUITAR PRACTICE TRACKER

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/n4v1ds0n/guitar-practice-tracker)](https://www.github.com/n4v1ds0n/guitar-practice-tracker/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/n4v1ds0n/guitar-practice-tracker)](https://www.github.com/n4v1ds0n/guitar-practice-tracker/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/n4v1ds0n/guitar-practice-tracker)](https://www.github.com/n4v1ds0n/guitar-practice-tracker)


![Am I Responsive](docs/am-i-responsive.PNG)

**Developer: Damian Droste**

💻 [Visit live website](https://<deploymentname>.herokuapp.com/)  
(Ctrl + click to open in new tab)


## Table of Contents
  - [About](#about)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Colours](#colours)
    - [Fonts](#fonts)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [Database](#database)
    - [Wireframes](#wireframes)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [Automated testing](#automated-testing)
    - [Tests on various devices](#tests-on-various-devices)
    - [Browser compatibility](#browser-compatibility)
  - [Bugs](#bugs)
  - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)



### 📋 About
The Guitar Practice Tracker is a web application designed to help guitarists set,
track, and achieve practice goals efficiently. It supports both custom and standard 
goals and provides detailed session logging, progress tracking, and user profile management.

### User Goals

- Set and Manage Goals:
	Users aim to set personal goals for different practice types—such as technique, routine, or repertoire—and break them into measurable targets.
- Log Practice Sessions Easily:
	Users want a clean, efficient interface to quickly log their daily or weekly practice sessions, optionally linking them to goals.
- Customize or Use Predefined Goals:
	Users should be able to either define their own goals or select from a curated list of standard goals for guidance.
- Upload practice recordings to compare their performances over time


### Site Owner Goals

- Offer a Valuable Learning Tool for Musicians:
	Provide a focused app that supports musical development through structured, goal-based practice.
- Ensure Secure, Personalized User Experience:
	Maintain account-based data with authentication, profile customization, and user-specific goal/session management.
- Promote Best Practices in Practice Planning:
	Help users understand and apply structured practice methods like routine scheduling and measurable targets.
- Provide Admin Tools for Goal Curation:
	Enable site admins to define standard goal templates that users can select and autofill into their own plans.
- Ensure Accessibility and Responsiveness:
	Deliver a clean, mobile-friendly UI that is usable and visually accessible across devices and screen sizes.
<hr>

## User Experience

### 🎯 Target Audience

- Guitarists of all skill levels who want to track their practice progress over time
- Students following a structured practice routine provided by a teacher or school
- Hobbyists who want to balance structured and creative practice
- Musicians preparing for performances, auditions, or recordings
- Anyone who enjoys goal-setting and wants to quantify their musical development

### User Requirements and Expectations

- Fully Responsive Design:
	The app must work seamlessly across desktops, tablets, and mobile devices so users can log sessions on the go.
- Accessibility:
	Clear contrast, readable fonts, and keyboard navigability ensure users with different abilities can interact with the app easily.
- Welcoming, Minimalist Design:
	Users expect a clutter-free interface that supports concentration and gives priority to functionality.
- Social & Support Links:
	Easy access to support or feedback forms, as well as links to relevant communities or help pages, adds to user trust.
- Clear Contact and Account Info:
	Users want to easily manage their profiles, see their progress, and optionally delete their data securely.
- Progress Visualization:
	Visual feedback like progress bars and session history boosts motivation and helps users stay committed.

##### Back to [top](#table-of-contents)<hr>

## User Stories

### Site Users

1. 	I want to create a personal user account so I can track my practice goals and sessions securely.

2. 	I want to log into my account so I can access my private dashboard and practice data. 

3. 	I want to log out easily so I can ensure my data is not accessible to others.

4. 	I want to navigate the site freely and explore all the features

5. 	I want to view an overview of my goals on the dashboard so I can stay focused on my current practice priorities.

6. 	I want to create a new goal so I can stay focused on my current practice priorities.

7. 	I want to select a goal type so I can define what I want to work on

8. 	I want to autofill a goal from a predefined list of standard goals so the app tailors the required input fields accordingly

9. 	I want to log a practice session so I can track the time I’ve spent and key metrics 

10. 	I want the session form to adjust to the selected goal type so irrelevant input fields are hidden

11. 	I want to view a list of all my past practice sessions so I can reflect on what I’ve done so far.

12. 	I want to link sessions to a specific goal so I can see my work in the context of a particular objective.

13.	I want to edit a goal or a session after creating it so I can fix mistakes or adjust targets.

14. 	I want to delete goals and sessions so I can clean up outdated or irrelevant data.

15.	I want to see my profile and update basic details like username and email so I stay in control of my account.

16. 	I want to upload or change a profile picture so my account feels more personal.

17. 	I want to delete my account so I can remove my data completely if I no longer want to use the app.



### Admin / Authorised User

18. 	I want to create and manage standard goal definitions so users have access to pre-built, structured goal templates.

19.	I want to view all registered users through the Django admin panel so I can monitor usage and manage inappropriate or inactive accounts.

20. 	I want to make certain fields required or optional at the model level so data integrity is preserved throughout the app.

21.	I want to test all user flows and forms directly in the admin panel so I can quickly identify and resolve edge cases or bugs.



### Site Owner/ Project Maintainer

22.	I want to deploy the project in a maintainable and scalable way so it can be hosted on a platform like Heroku or Render with minimal downtime.

23. 	I want to structure the code with reusable components so future features like progress charts or notifications can be added easily.

24. 	I want to include documentation (like this README) so other developers can understand and contribute to the project easily.

25. 	I want to integrate basic accessibility and responsive design best practices so the app is usable across devices and for users with diverse needs.  

26. 	As a Site Owner I can edit data entered into my site so that all submitted data is maintained to avoid errors


### Kanban, Epics & User Stories
- GitHub was used to track all open user stories
- Epics were created using the milestones feature
- Backlog, In Progress, Done headings were used in a board

<details><summary>Epics</summary>
<img src="docs\github_project\closedepics.png">
Epics
<img src="docs\github-project\EPIC1.png">
Epic 1
<img src="docs\github-project\EPIC2.png">
Epic 2
<img src="docs\github-project\EPIC3.png">
Epic 3
<img src="docs\github-project\EPIC4.png">
Epic 4
<img src="docs\github-project\EPIC5.png">
Epic 5
<img src="docs\github-project\EPIC6.png">
Epic 6
<img src="docs\github-project\EPIC7.1.png">
Epic 7 (closed items)
<img src="docs\github-project\EPIC7.2.png">
Epics 7 (open items)

Section for future endeavours:

<img src="docs\github-project\openepics.png">
open Epics
<img src="docs\github-project\EPIC8.png">
Epic 8
</details>

<details><summary>User Stories</summary>
<img src="docs\github-project\userstories.png">
User Stories
</details>

<details><summary>Kanban</summary>
<img src="docs\github-project\userstories.png">
View of the Board
</details>

## Design

### Colours

I chose warm and and vintage colours while maintaining a modern design. I wanted the app to look like a modern offspring of my custom guitar shop which uses the same colour palette. 

The colors I wanted to stay close to  [Coolors.co](https://coolors.co/)
<details><summary>See colour pallet</summary>
<img src="docs\design\color-palettte.png">
</details>

### Fonts

 The fonts selected were from Google Fonts, Montserrat wits sans-serif as a backup font.
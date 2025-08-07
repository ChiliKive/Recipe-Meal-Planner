# 🍽️ Recipe Meal Planner – Project Vision (Draft)

## 🔧 Functionality Overview

### 👤 User Account
- Each user has an account and can log in to the system.
- The account stores:
  - Saved meals (recipes)
  - Personal user information
  - Automatic calculation of daily nutritional needs (Calories, Proteins, Fats, Carbohydrates)

---

### 📅 Meal Plans (Rations)
- Users can create **weekly** or **daily** meal plans (called *Rations*).
- Each Ration:
  - Can have a custom name
  - Is composed of one or more Meals (Recipes)
  - Aggregates total nutritional values from all included Meals

---

### 🍲 Meals (Recipes)
- A Meal consists of:
  - A list of **Ingredients**
  - A step-by-step **Recipe** (instructions)
  - Optionally: a photo of the dish
- Nutritional information for each Meal is calculated based on its ingredients.

---

### 🥦 Ingredients
- Ingredient data will be fetched from a public **Food API** (e.g., USDA or Edamam).
- Each Ingredient contains:
  - Name
  - Quantity + unit
  - Nutritional values (kcal, protein, fat, carbs)

---

## 🧠 High-Level Concept

A website where users can:
1. Log in
2. Create and save multiple personalized Rations (daily or weekly plans)
3. View their current active Ration on the homepage
4. Build Rations using Meals, and Meals using Ingredients
5. Automatically calculate nutritional values to see if a Ration matches their daily needs

---

## 🗂️ Pages and Features

### Home Page
- Shows the currently selected active Ration (e.g., this week's plan)

### Rations Page
- View all user-created Rations
- Filter by type: daily or weekly
- Create new Rations
- Possibly mark Rations as **public** or **private** (for future sharing)

### Meals Page
- View all user-created Meals
- Add new Meals with ingredients and preparation steps
- Upload a photo of the dish

---

## 🔄 Notes for Future Features
- Public Meal/Ration sharing and browsing
- Ability to clone a Ration or copy days
- No full calorie tracking at this stage
- Matching user's Kcal/macros against Rations (just for display)


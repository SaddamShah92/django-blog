# Django Blog & Portfolio Platform

A full-featured, role-based blogging platform built with **Django** (backend) and **Bootstrap** (frontend). Started as a personal practice project and evolved into a complete functional application with separate dashboards for different user roles, a personal portfolio section, and dynamic content management.

Live Demo: 

## Features

- **Role-Based Access Control (RBAC)**:
  - **Admin**: Full access (create/manage users, assign roles, all content)
  - **Manager**: Manages editors and approves/oversees blogs
  - **Editor**: Creates, edits, and manages blog posts only
  - **Authenticated Users**: Can read blogs, log in to comment, and access a personal dashboard
  - **Anonymous Users**: Can only read blogs (no commenting)

- **Blog System**:
  - Multi-category blogs (Sports, Politics, Technology, Business, Health, Science, etc.)
  - Rich text editing, images, dynamic categories
  - Comments (authenticated users only)
  - Search functionality

- **Portfolio Section**:
  - Dedicated page showcasing personal projects, skills, and details

- **Dynamic About & Social Links**:
  - Editable about section and social media icons

- **Separate Dashboards**:
  - Custom frontend dashboards for Editor and Manager roles (no need for admin panel access)

- **Responsive Design**:
  - Fully mobile-friendly with Bootstrap 5

- **Other**:
  - User registration, login, logout
  - Admin panel enhancements
  - Clean separation of apps for maintainability

## Project Structure

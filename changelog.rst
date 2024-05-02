Changelog
*********

.. _v4.6:

4.6
===

* *Release: 10 May 2024*

* **Features:**

  * Added information to Project Settings that the Project Template has to be shared with others in order to be visible
  * Reworked cancel buttons in create forms

* **Bugfixes**

  * Fixed some parts of Project were not accessible when Project was shared with a public link in edit mode
  * Fixed comments in threads in Projects had random order
  * Fixed routing after clicking on Cancel in several Create forms
  * Fixed redirect after log in from public questionnaire
  * Fixed Markdown newlines using \ would not render correctly in Document
  * Fixed delete buttons in Submission Service settings would submit the whole form
  * Fixed Submission Settings had Save button even when there was no change
  * Fixed create new Document Template form would suggest a wrong version number
  * Fixed some menu items were only partially clickable
  * Fixed rare wrong rendering of icons

.. _v4.5.2-backend:

4.5.2 (backend)
===============

* *Release: 15 April 2024*

* **Bugfixes**

  * Fixed bottleneck in metric and indication computations

.. _v4.5.1-backend:

4.5.1 (backend)
===============

* *Release: 9 April 2024*

* **Bugfixes**

  * No visible changes to users

.. _v4.5.2-frontend:

4.5.2 (frontend)
================

* *Release: 8 April 2024*

* **Bugfixes**

  * No visible changes to users

.. _v4.5.1-frontend:

4.5.1 (frontend)
================

* *Release: 5 April 2024*

* **Bugfixes**

  * Fixed style customizations

.. _v4.5:

4.5
===

* *Release: 2 April 2024*

* **Features:**

  * Added hide option in secrets settings
  * Added consistent spacing for settings items
  * Improved selected tags in project settings to clarify which tags are selected

* **Bugfixes:**

  * Fixed problem that URL input would not be recognized as URL in textbox fields in forms

.. _v4.4.1-backend:

4.4.1 (backend)
===============

* *Release: 15 April 2024*

* **Bugfixes**

  * Fixed bottleneck in metric and indication computations

.. _v4.4.1-tools:

4.4.1 (tools)
=============

* *Release: 19 March 2024*

* **Bugfixes:**

  * Fixed color handling in mailer

.. _v4.4:

4.4
===

* *Release: 6 March 2024*

* **Features:**

  * Added create project from template from projects list dropdown menu
  * Improved project creation form
  * Improved move functionality in knowledge model editor with highlighting item that is being moved
  * Adjusted color of non-desirable questions

* **Bugfixes:**

  * Fixed downloading documents from read-only sharing projects would not work
  * Fixed migrating project would not change "updated at" value

.. _v4.3.2-tools:

4.3.2 (tools)
=============

* *Release: 19 March 2024*

* **Bugfixes:**

  * Fixed color handling in mailer

.. _v4.3.1-backend:

4.3.1 (backend)
===============

* *Release: 26 February 2024*

* **Bugfixes:**

  * No visible changes to users

.. _v4.3.1-tools:

4.3.1 (tools)
=============

* *Release: 21 February 2024*

* **Bugfixes:**

  * Fixed getting config in mailer for Registry

.. _v4.3:

4.3
===

* *Release: 6 February 2024*

* **Features:**

  * Added possibility to import document templates from registry if unsupported metamodel using update badge
  * Added information who created the feedback to GitHub issue

* **Bugfixes:**

  * Fixed wrong special characters coding in machine actionable formats
  * Fixed unclear error message for forgotten password
  * Fixed TDK watch mode errors after descriptor change
  * Fixed typehints for public projects

.. _v4.2.2-backend:

4.2.2 (backend)
===============

* *Release: 1 February 2024*

* **Bugfixes:**

  * Fixed wrongly shown project tags

.. _v4.2.2-frontend:

4.2.1 (frontend)
================

* *Release: 24 January 2024*

* **Bugfixes:**

  * Fixed project typehints for anonymous users

.. _v4.2.1-backend:

4.2.1 (backend)
===============

* *Release: 24 January 2024*

* **Bugfixes:**

  * Fixed cleaning temporary-generated documents


.. _v4.2.1-tools:

4.2.1 (tools)
=============

* *Release: 8 January 2024*

* **Security:**

  * Use Jinja2 sandboxed environment for document generation.
  * Fixed CVE-2023-7104.


.. _v4.2:

4.2
===

* *Release: 2 January 2024*

* **Bugfixes:**

  * Fixed unset project from document template editor preview on deletion of project.
  * Fixed knowledge model editor buttons position for small screens.
  * Fixed not unfolding project actions menu.
  * Fixed wrong link to SDK in widget integration URL description.

.. _v4.1.1-frontend:

4.1.1 (frontend)
================

* *Release: 18 December 2023*

* **Bugfixes:**

  * Fixed links to questions in questionnaires.


.. _v4.1.2-tools:

4.1.2 (tools)
=============

* *Release: 8 January 2024*

* **Security:**

  * Use Jinja2 sandboxed environment for document generation.
  * Fixed CVE-2023-7104.


.. _v4.1.1-tools:

4.1.1 (tools)
=============

* *Release: 12 December 2023*

* **Bugfixes:**

  * Fixed retry mechanism for command queue used in workers.


.. _v4.1.1-backend:

4.1.1 (backend)
===============

* *Release: 11 December 2023*

* **Bugfixes:**

  * Fixed upgrading the Document Template metamodel version for Document Template Editors.


.. _v4.1:

4.1
===

* *Release: 5 December 2023*

* **Features:**

  * Added project actions and created new `integration SDK <https://github.com/ds-wizard/dsw-integration-sdk>`__ for that and other existing integrations.

* **Bugfixes:**

  * Fixed primary color that didn't work correctly on some elements after 4.0 rework.
  * Fixed Jinja2 template error reporting when generating documents.
  * Fixed pagination after deleting last items in listings.

* **Misc:**

  * Unified UID and GID in Docker images.


.. _v4.0.1-tools:

4.0.1 (tools)
=============

* *Release: 12 December 2023*

* **Bugfixes:**

  * Fixed retry mechanism for command queue used in workers.


.. _v4.0.3-frontend:

4.0.3 (frontend)
================

* *Release: 1 December 2023*

* No visible changes to users.


.. _v4.0.2-frontend:

4.0.2 (frontend)
================

* *Release: 20 November 2023*

* **Bugfixes:**

  * Fixed links to other apps.
  * Fixed clearing tokens after logout.


.. _v4.0.1-backend:

4.0.1 (backend)
===============

* *Release: 14 November 2023*

* **Bugfixes:**

  * Fixed duplicate documents in document lists.


.. _v4.0.1-frontend:

4.0.1 (frontend)
================

* *Release: 14 November 2023*

* **Bugfixes:**

  * Fixed OpenID login buttons.
  * Fixed favicon.

* **Misc:**

  * Removed style version from about dialog (as it is no longer used since 4.0).


.. _v4.0:

4.0
===

* *Release: 13 November 2023*

* **Features:**

  * Introduced nested routes, client now runs on ``/wizard`` and server on ``/wizard-api``, so that both can run on single subdomain.
  * SASS was removed from the client image, and styling options have been reworked.
  * Integration response is now shown as plain text in the questionnaire version history, so the raw Markdown code is not visible there.
  * Added focus to the first input field when adding a new or opening an existing entity in the KM editor.

* **Bugfixes:**

  * Fixed non-desirable follow-up questions in questionnaires so there is no empty box.
  * Fixed warnings for deleted entities in the KM editor.
  * Fixed watch mode termination in TDK in some cases.
  * Fixed creating templates with brackets in name in TDK.


.. _v3.28:

3.28
====

* *Release: 3 October 2023*

* **Features:**

  * Added a button to add another sibling entity in the navigation tree in the knowledge model editor.
  * Question tags are now preselected when creating a project migration if they were used in the original project.
  * Error is now shown in the user create form when the email is already used.
  * Added support for more fonts in PDF documents.
  * Improve the performance of knowledge model editors and projects.

* **Bugfixes:**

  * Fixed selecting of knowledge model on project creation after the selected knowledge model was removed.
  * Fixed user filter on the project list after unselecting a user and selecting another one.
  * Fixed preview of files with incompatible character encoding.
  * Fixed questionnaire navigation tree showing non-desirable questions when they should be hidden.
  * Fixed minor issues in document template selection when creating a new document.
  * Fixed integration in KM editor showing deleted questions are used.

* **Misc:**

  * Changed the default user role from data steward to researcher when a new wizard instance is started.


.. _v3.27.1-tools:

3.27.1 (tools)
==============

* *Release: 20 September 2023*

* **Bugfixes:**

  * Fix detection of PDF output document format.


.. _v3.27.1-backend:

3.27.1 (backend)
================

* *Release: 20 September 2023*

* **Bugfixes:**

  * Fixed document template formats that didn't work under certain conditions.


.. _v3.27.1-frontend:

3.27.1 (frontend)
=================

* *Release: 7 September 2023*

* **Security:**

  * Fixed CVE-2023-32559 and CVE-2023-32002.


.. _v3.27:

3.27
====

* *Release: 5 September 2023*

* **Features:**

  * Added notification emails about newly created and expiring API keys.
  * Added explicit info when there are no questions in an item.

* **Bugfixes:**

  * Fixed filters on list views when changing filters while items are loading.
  * Fixed project tags filter when removing last tag.
  * Fixed Life Science Login badge.

* **Miscs:**

  * Removed credentials authentication from TDK, API keys should be used instead.


.. _v3.26.2-tools:

3.26.2 (tools)
==============

* *Release: 20 September 2023*

* **Bugfixes:**

  * Fix detection of PDF output document format.


.. _v3.26.1-backend:

3.26.1 (backend)
================

* *Release: 20 September 2023*

* **Bugfixes:**

  * Fixed document template formats that didn't work under certain conditions.


.. _v3.26.1-tools:

3.26.1 (tools)
==============

* *Release: 10 August 2023*

* **Bugfixes:**

  * Fixed loading custom mail config in mailer.


.. _v3.26.1-frontend:

3.26.1 (frontend)
=================

* *Release: 10 August 2023*

* **Bugfixes:**

  * Fixed the knowledge model filter on the project list.


.. _v3.26:

3.26
====

* *Release: 1 August 2023*

* **Features:**

  * Added explicit info when there are no questions in a chapter.
  * Comments tab is now highlighted when comments are open on a specific question.

* **Bugfixes:**

  * Fixed cursor on radio input in the document template format selection.
  * Fixed file upload UI in the document template editor.
  * Fixed description in Markdown inputs.
  * Fixed deleting queued documents (the dropdown menu was sometimes disappearing).
  * Fixed link to document template development from the Data Steward dashboard.
  * Fixed displaying of alphabetical identifiers for answers, choices, and items.

* **Misc:**

  * Default role was changed to Researcher when running a fresh instance.
  * Deleting users is now much faster.
  * Upgraded Bootstrap to 5.3.0 in frontend.

* **More:**

  * `API Changelog 3.25.0 ➔ 3.26.0 <https://api-docs.ds-wizard.org/changelogs/3.25.0-3.26.0.html>`__

.. _v3.25.1-tools:

3.25.1 (tools)
==============

* *Release: 10 August 2023*

* **Bugfixes:**

  * Fixed loading custom mail config in mailer.

.. _v3.25.3-frontend:

3.25.3 (frontend)
=================

* *Release: 10 August 2023*

* **Bugfixes:**

  * Fixed the knowledge model filter on the project list.

.. _v3.25.1-backend:

3.25.1 (backend)
=================

* *Release: 19 July 2023*

* **Bugfixes:**

  * Fixed user activation when logging in for the first time using OpenID, and no Terms of Service or Privacy Policy were set.

.. _v3.25.2-frontend:

3.25.2 (frontend)
=================

* *Release: 18 July 2023*

* **Bugfixes:**

  * Fixed preview of item questions in KM Editor that could sometimes cause two items to have the same value when filling them in.

.. _v3.25.1-frontend:

3.25.1 (frontend)
=================

* *Release: 6 July 2023*

* **Bugfixes:**

  * Fixed change logo button in settings (affects only instances where this is enabled).

.. _v3.25:

3.25
====

* *Release: 4 July 2023*

* **Features:**

  * Added revoke all to `active sessions <https://guide.ds-wizard.org/en/3.25/application/profile/edit/active-sessions.html>`__.
  * Added Terms of Service and/or Privacy agreement confirmation during SSO sign up when they are set.
  * `Preview in KM Editor <https://guide.ds-wizard.org/en/3.25/application/knowledge-models/editors/detail/preview.html#km-editor-preview>`__ now opens on current question (corresponding answers are pre-selected if the question is nested).
  * Improved `phase selection <https://guide.ds-wizard.org/en/3.25/application/projects/list/detail/questionnaire.html#questionnaire-current-phase>`__ in questionnaire and phase description is now used.
  * Improved question tags selection when `creating a new project <https://guide.ds-wizard.org/en/3.25/application/projects/list/create.html#create-project-custom>`__ to make it more clear which questions will be used.
  * Added support for uploading more files in document template editor.

* **Bugfixes:**

  * Fixed links from TODOs or comments to questions in collapsed items (they now expand).
  * Fixed SMTP configuration without username and password for authentication.

* **Misc:**

  * Added *robots.txt* to client and server to prevent indexing of the applications.

* **More:**

  * `API Changelog 3.24.0 ➔ 3.25.0 <https://api-docs.ds-wizard.org/changelogs/3.24.0-3.25.0.html>`__

.. _v3.24.1-frontend:

3.24.1 (frontend)
=================

* *Release: 6 July 2023*

* **Bugfixes:**

  * Fixed change logo button in settings (affects only instances where this is enabled).

.. _v3.24.1-backend:

3.24.1 (backend)
================

* *Release: 14 June 2023*

* **Bugfixes:**

  * Fixed generating documents that contain more than one whitespace in the filename.

* **More:**

  * `API Changelog 3.24.0 ➔ 3.24.1 <https://api-docs.ds-wizard.org/changelogs/3.24.0-3.24.1.html>`__

.. _v3.24:

3.24
====

* *Release: 30 May 2023*

* **Features:**

  * List views (such as project list or knowledge model list) have been reworked so that only the results are reloaded instead of the whole page. Therefore, the search field should not loose focus when typing slowly.
  * Added warning before the user session expires.
  * Improved information on detail pages (such as knowledge model or document template).

* **Bugfixes:**

  * Fixed document generation when there were inconsistent replies after questionnaire migration.
  * Fixed icon alignment in questionnaire import.
  * Fixed color transition for menu icons.

* **Misc:**

  * All document templates from DSW Registry now use WeasyPrint instead of wkhtmltopdf for PDF formats.
  * It is recommended to migrate your existing PDF template to `WeasyPrint <https://github.com/ds-wizard/engine-tools/blob/develop/packages/dsw-document-worker/support/steps/weasyprint.md>`__ as wkhtmltopdf will be removed in the future.

* **More:**

  * `API Changelog 3.23.0 ➔ 3.24.0 <https://api-docs.ds-wizard.org/changelogs/3.23.0-3.24.0.html>`__

.. _v3.23.3-backend:

3.23.3 (backend)
================

* *Release: 14 June 2023*

* **Bugfixes:**

  * Fixed generating documents that contain more than one whitespace in the filename.

* **More:**

  * `API Changelog 3.23.2 ➔ 3.23.3 <https://api-docs.ds-wizard.org/changelogs/3.23.2-3.23.3.html>`__

.. _v3.23.2-backend:

3.23.2 (backend)
================

* *Release: 25 May 2023*

* **Bugfixes:**

  * Fixed API key expiration to use the value set when creating it.

* **More:**

  * `API Changelog 3.23.1 ➔ 3.23.2 <https://api-docs.ds-wizard.org/changelogs/3.23.1-3.23.2.html>`__

.. _v3.23.1-backend:

3.23.1 (backend)
================

* *Release: 4 May 2023*

* **Bugfixes:**

  * Fixed loading RSA private key if set only in the ENV variable.

* **More:**

  * `API Changelog 3.23.0 ➔ 3.23.1 <https://api-docs.ds-wizard.org/changelogs/3.23.0-3.23.1.html>`__

.. _v3.23:

3.23
====

* *Release: 2 May 2023*

* **Features:**

  * Added the possibility to generate `API keys <https://guide.ds-wizard.org/en/3.23/application/profile/edit/api-keys.html#api-keys>`__ to access the API instead of using username and password. The API keys also work when 2FA is enabled.
  * Added an overview of all `active sessions <https://guide.ds-wizard.org/en/3.23/application/profile/edit/active-sessions.html>`__.
  * It is now possible to use HTML for `login info <https://guide.ds-wizard.org/en/3.23/application/administration/settings/user-interface/dashboard-and-login-screen.html#login-info>`__.
  * Added possibility for `sidebar login info <https://guide.ds-wizard.org/en/3.23/application/administration/settings/user-interface/dashboard-and-login-screen.html#sidebar-login-info>`__ under the login box.
  * Welcome warning and info have been reworked to `announcements <https://guide.ds-wizard.org/en/3.23/application/administration/settings/user-interface/dashboard-and-login-screen.html#announcements>`__ -- it is now possible to have an unlimited list of announcements of different levels and choose if they are visible on the dashboard and/or login screen.
  * Added sort by created to document template list.
  * Improved progress bar in project migration.
  * The warnings tab in the knowledge model editor is now automatically closed when the last one is resolved.
  * Improved form actions to make them more visible when forms change.

* **Bugfixes:**

  * Fixed project indication calculation after import or project migration.
  * Fixed double error message when deleting failed in list views.
  * Fixed buttons in email templates in Outlook.
  * Fixed phase in a questionnaire after project migration if the phase no longer exists.
  * Fixed dropdown menus in the sidebar when the page was scrolled.
  * Fixed knowledge model export from the knowledge model list.

* **Misc:**

  * Speed up processing and generating of documents.

* **More:**

  * `API Changelog 3.22.0 ➔ 3.23.0 <https://api-docs.ds-wizard.org/changelogs/3.22.0-3.23.0.html>`__

.. _v3.22.1-tools:

3.22.1 (tools)
==============

* *Release: 14 April 2023*

* **Bugfixes:**

  * Fixed sending mails when configuration is loaded from database.

.. _v3.22.3-backend:

3.22.3 (backend)
================

* *Release: 13 April 2023*

* **Bugfixes:**

  * Fixed the selected phase in projects when migrating from a knowledge model without phases to a knowledge model with phases.

* **More:**

  * `API Changelog 3.22.2 ➔ 3.22.3 <https://api-docs.ds-wizard.org/changelogs/3.22.2-3.22.3.html>`__

.. _v3.22.2-backend:

3.22.2 (backend)
================

* *Release: 12 April 2023*

* **Bugfixes:**

  * Fixed an issue that sometimes caused suggesting the same knowledge model multiple times when creating a new project or knowledge model editor.

* **More:**

  * `API Changelog 3.22.1 ➔ 3.22.2 <https://api-docs.ds-wizard.org/changelogs/3.22.1-3.22.2.html>`__

.. _v3.22.1-frontend-backend:

3.22.1 (frontend, backend)
==========================

* *Release: 11 April 2023*

* **Bugfixes:**

  * Fixed database migration of existing KM editors after 3.22 that could cause unexpected KM editor version or missing metadata (such as readme).
  * Fixed publish process in KM editor and Document Template Editor that could be confusing after 3.22 changes.
  * Fixed deleting KM editor when it is migrating.

* **More:**

  * `API Changelog 3.22.0 ➔ 3.22.1 <https://api-docs.ds-wizard.org/changelogs/3.22.0-3.22.1.html>`__

.. _v3.22:

3.22
====

* *Release: 4 April 2023*

* **Features:**

  * Added the possibility to set a knowledge model as deprecated so researchers cannot use it to create new projects.
  * Added `phase editor <https://guide.ds-wizard.org/en/3.22/application/knowledge-models/editors/detail/phases.html#km-editor-phases>`__ to KM Editor (similar to Tag editor).
  * Renamed `Template` tab to `Settings` in the document template editor to make it consistent with KM Editor or Project.
  * Added link to selected project in document template editor preview.
  * Position in the questionnaire is now remembered when switching tabs in the project (such as going to preview and back to the questionnaire).
  * Warnings tab in the project is now automatically closed when the last one is resolved.
  * Projects are no longer filtered by current user if the user is admin.
  * Improved accessibility of unanswered question indications and metrics (as well as adding an option to hide non-desirable questions).
  * Added information about a version of all components in the About modal.
  * Improved add button labels in various forms to make it easier to understand what they add.
  * Added support for DKIM signing for emails.
  * Added experimental `weasyprint step <https://github.com/ds-wizard/engine-tools/blob/develop/packages/dsw-document-worker/support/steps/weasyprint.md>`__ in document templates for better PDF documents generation.
  * User details are now updated in the menu after editing your own profile.
  * Added link to the DSW Registry from locale detail.

* **Bugfixes:**

  * Fixed visible first chapter in KM Editor preview when deleted.
  * Fixed inconsistent update label for badge and action for KM migration.
  * Fixed failing to publish knowledge models due to wrong event squashing in some cases.
  * Fixed redirect to login when opening the project after the session has expired.
  * Fixed a visual bug in the project selection dropdown in the document template editor preview.
  * Fixed text overflow for long questions/answers in the project import view.
  * Fixed image previews in the document template editor.
  * Fixed downloading document template with DSW TDK.
  * Fixed dropdown menu separators in list views.

* **Misc:**

  * Added support for RO-Crates (`RO-Crate Importer <https://github.com/ds-wizard/dsw-ro-crate-importer>`__ and `RO-Crate Template <https://github.com/ds-wizard/ro-crate-template>`__)
  * Improved default English locale metadata.
  * Added support for arm64 builds for most of the Docker images.

* **More:**

  * `API Changelog 3.21.0 ➔ 3.22.0 <https://api-docs.ds-wizard.org/changelogs/3.21.0-3.22.0.html>`__

.. _v3.21:

3.21
====

* *Release: 7 March 2023*
* **Key changes:**
  
  * Two-factor authentication (2FA)
  * i18n support in document templates
  * RO-Crate import/export
  * Warnings on imports
  * Various optimizations and UI fixes

.. _v3.20.3-frontend:

3.20.3 (frontend)
=================

* *Release: 21 February 2023*
* **Key changes:**
  
  * Fix vulnerabilities in the base image

.. _v3.20.2-frontend:

3.20.2 (frontend)
=================

* *Release: 10 February 2023*
* **Key changes:**
  
  * Fix based on when creating new document template

.. _v3.20.2-tools:

3.20.2 (tools)
==============

* *Release: 10 February 2023*
* **Key changes:**
  
  * Fix updating template.json using TDK
  * Fix retrieving app config and questionnaire for documents

.. _v3.20.1-tools:

3.20.1 (tools)
==============

* *Release: 9 February 2023*
* **Key changes:**
  
  * Fix creating document template draft from TDK

.. _v3.20.1-frontend:

3.20.1 (frontend)
=================

* *Release: 8 February 2023*
* **Key changes:**
  
  * Fix document template detail in registry

.. _v3.20:

3.20
====

* *Release: 7 February 2023*
* **Key changes:**
  
  * Document template editor (`idea <https://ideas.ds-wizard.org/posts/10/document-template-editor>`__)
  * Mark document template as legacy
  * Various UI improvements and fixes

.. _v3.19.3-backend:

3.19.3 (backend)
================

* *Release: 17 January 2023*
* **Key changes:**
  
  * Fix importing KM if file contains .ttl

.. _v3.19.2-tools:

3.19.2 (tools)
==============

* *Release: 17 January 2023*
* **Key changes:**
  
  * Fix version identification in tools

.. _v3.19.1-tools:

3.19.1 (tools)
==============

* *Release: 15 January 2023*
* **Key changes:**
  
  * Fix path serialization in TDK

.. _v3.19.2-backend:

3.19.2 (backend)
================

* *Release: 12 January 2023*
* **Key changes:**
  
  * Fix synchronization of locales from Registry

.. _v3.19.1-frontend:

3.19.1 (frontend)
=================

* *Release: 6 January 2023*
* **Key changes:**
  
  * Fix narrow panel in project import view

.. _v3.19.1-backend:

3.19.1 (backend)
================

* *Release: 3 January 2023*
* **Key changes:**
  
  * Fix loading string variable from env

.. _v3.19:

3.19
====

* *Release: 3 January 2023*
* **Key changes:**
  
  * Indications computation
  * Minor UI improvements and fixes

.. _v3.18.4-backend:

3.18.4 (backend)
================

* *Release: 16 December 2022*
* **Key changes:**
  
  * Fix app limit recompute

.. _v3.18.3-frontend:

3.18.3 (frontend)
=================

* *Release: 15 December 2022*
* **Key changes:**
  
  * Fix fallback to default in plural locale strings

.. _v3.18.3-backend:

3.18.3 (backend)
================

* *Release: 2 December 2022*
* **Key changes:**
  
  * Add LOC_PERM in default Admin perms
  * Fix deleting comment threads
  * Fix not sending a questionnaire event uuid when creating document

.. _v3.18.2-frontend:

3.18.2 (frontend)
=================

* *Release: 1 December 2022*
* **Key changes:**
  
  * Fix resolving default locale

.. _v3.18.2-backend:

3.18.2 (backend)
================

* *Release: 1 December 2022*
* **Key changes:**
  
  * Fix resolving default locale

.. _v3.18.1-frontend:

3.18.1 (frontend)
=================

* *Release: 1 December 2022*
* **Key changes:**
  
  * Fix import link from outdated KM alert

.. _v3.18.1-backend:

3.18.1 (backend)
================

* *Release: 1 December 2022*
* **Key changes:**
  
  * Fix description, readme and primary key for locale
  * Fix creating locale when app is registered

.. _v3.18:

3.18
====

* *Release: 29 November 2022*
* **Key changes:**
  
  * Localizations (`idea <https://ideas.ds-wizard.org/posts/23/translate-into-other-languages>`__)
  * Filter file extensions when importing KM or template
  * Logout user when 401 received from API on dashboard

.. _v3.17.1-frontend:

3.17.1 (frontend)
=================

* *Release: 14 November 2022*
* **Key changes:**
  
  * Fix security vulnerabilities in base image

.. _v3.17:

3.17
====

* *Release: 1 November 2022*
* **Key changes:**
  
  * Consistency checks before publishing KM (`idea <https://ideas.ds-wizard.org/posts/77/check-some-consistency-before-publishing-new-km>`__)
  * Filter projects by KM (`idea <https://ideas.ds-wizard.org/posts/87/filter-projects-by-km>`__)
  * Support for ZIP/TAR archives and Excel exports
  * Use of gettext for client localizations
  * Support for OpenID logout functionality

.. _v3.16.3-backend:

3.16.3 (backend)
================

* *Release: 27 October 2022*
* **Key changes:**
  
  * Fix parsing datetime from database

.. _v3.16.2-backend:

3.16.2 (backend)
================

* *Release: 12 October 2022*
* **Key changes:**
  
  * Remove KnowledgeModelCache, PackageCache, QuestionnaireContentCache, and QuestionnaireReportCache

.. _v3.16.1-backend:

3.16.1 (backend)
================

* *Release: 6 October 2022*
* **Key changes:**
  
  * Fix synchronizing feedback issues
  * Fix deleting user when user is set to createdBy in KM editor and questionnaire
  * Fix questionnaire recompute job

.. _v3.16:

3.16
====

* *Release: 4 October 2022*
* **Key changes:**
  
  * Import for replies from other questionnaires (`idea <https://ideas.ds-wizard.org/posts/5/import-answers-to-questionnaires>`__)
  * Collapsible and movable items in list questions
  * Main menu grouping
  * Speed optimizations and refactoring

.. _v3.15.3-tools:

3.15.3 (tools)
==============

* *Release: 17 September 2022*
* **Key changes:**
  
  * Fix worker on-start DB query memory leaks

.. _v3.15.1-backend:

3.15.1 (backend)
================

* *Release: 14 September 2022*
* **Key changes:**
  
  * Add nonce to OpenID

.. _v3.15.2-frontend:

3.15.2 (frontend)
=================

* *Release: 14 September 2022*
* **Key changes:**
  
  * Add nonce to OpenID

.. _v3.15.2-tools:

3.15.2 (tools)
==============

* *Release: 7 September 2022*
* **Key changes:**
  
  * Fix timezone for job retrieval in workers

.. _v3.15.1-frontend:

3.15.1 (frontend)
=================

* *Release: 7 September 2022*
* **Key changes:**
  
  * Fix document and project template labels

.. _v3.15.1-tools:

3.15.1 (tools)
==============

* *Release: 7 September 2022*
* **Key changes:**

  * Fix document generation exception handling

.. _v3.15:

3.15
====

* *Release: 5 September 2022*
* **Key changes:**
  
  * Project loading optimization
  * Python components refactoring
  * Several other fixes and refactoring

.. _v3.14.1-tools:

3.14.1 (tools)
==============

* *Release: 4 August 2022*
* **Key changes:**
  
  * Fix package-data in dsw-tdk (`new` command)

.. _v3.14.1-backend:

3.14.1 (backend)
================

* *Release: 4 August 2022*
* **Key changes:**
  
  * Fix document preview for anonymous users
  * Fix OpenID and template export endpoints not to require a transaction

.. _v3.14:

3.14
====

* *Release: 2 August 2022*
* **Key changes:**
  
  * Migrate to Bootstrap 5
  * Improve authentication for downloads
  * Python components refactoring

.. _v3.13:

3.13
====

* *Release: 28 June 2022*
* **Key changes:**
  
  * Prevent user leave unsaved changes
  * Improved exceptions monitoring

.. _v3.12.1-tools:

3.12.1 (tools)
==============

* *Release: 13 June 2022*
* **Key changes:**
  
  * Fix document context for anonymous projects

.. _v3.12.1-backend:

3.12.1 (backend)
================

* *Release: 5 June 2022*
* **Key changes:**
  
  * Fix DB pool

.. _v3.12:

3.12
====

* *Release: 31 May 2022*
* **Key changes:**
  
  * New types of value questions
  * KM events optimizations
  * Several bugfixes and UI/UX improvements

.. _v3.11:

3.11
====

* *Release: 3 May 2022*
* **Key changes:**
  
  * Apply all action for KM migrations
  * Improved efficiency of document worker
  * Auto-upgrade default document templates in project
  * Several bugfixes and UI improvements

.. _v3.10.1-backend:

3.10.1 (backend)
================

* *Release: 17 April 2022*
* **Key changes:**
  
  * Fix settings API
  * Exclude common exceptions from Sentry logging

.. _v3.10.2-frontend:

3.10.2 (frontend)
=================

* *Release: 17 April 2022*
* **Key changes:**
  
  * Fix settings API

.. _v3.10.1-frontend:

3.10.1 (frontend)
=================

* *Release: 6 April 2022*
* **Key changes:**
  
  * Fix style builder

.. _v3.10:

3.10
====

* *Release: 5 April 2022*
* **Key changes:**
  
  * Mailer
  * Integration widget
  * Opening Markdown links in new tab/window
  * Several bugfixes and UI improvements

.. _v3.9.1-backend:

3.9.1 (backend)
===============

* *Release: 8 March 2022*
* **Key changes:**
  
  * Fix project migration when there are some documents

.. _v3.9:

3.9
===

* *Release: 1 March 2022*
* **Key changes:**
  
  * Basic password requirements
  * KM Editor: list of questions used with integration
  * Improved project migration
  * Usage statistics for administrators
  * Several bugfixes and UI improvements

.. _v3.8.2-backend:

3.8.2 (backend)
===============

* *Release: 14 February 2022*
* **Key changes:**
  
  * Fix questionnaire migration with move
  * Fix squashing KM editor events when publishing KM package

.. _v3.8.1-backend:

3.8.1 (backend)
===============

* *Release: 2 February 2022*
* **Key changes:**
  
  * Fix version ordering for KM package and templates in Registry

.. _v3.8.1-frontend:

3.8.1 (frontend)
================

* *Release: 1 February 2022*
* **Key changes:**
  
  * Fix KM Editor state

.. _v3.8:

3.8
===

* *Release: 1 February 2022*
* **Key changes:**
  
  * Online collaboration in KM Editor

.. _v3.7:

3.7
===

* *Release: 4 January 2022*
* **Key changes:**
  
  * Projects tagging and filtering

.. _v3.6.1-tools:

3.6.1 (tools)
=============

* *Release: 9 December 2021*
* **Key changes:**
  
  * Fix document context objectify with tags

.. _v3.6:

3.6
===

* *Release: 7 December 2021*
* **Key changes:**
  
  * Enhancing integration question options (item template)

.. _v3.5:

3.5
===

* *Release: 2 November 2021*
* **Key changes:**
  
  * Additional metadata for KM entities
  * Improved document submissions
  * Admin operations

.. _v3.4:

3.4
===

* *Release: 5 October 2021*
* **Key changes:**
  
  * Comments in projects
  * New Jinja filters for document context handling

.. _v3.3:

3.3
===

* *Release: 8 September 2021*
* **Key changes:**
  
  * Improved default document template
  * Improved template development experience
  * Enhanced Search API
  * Several fixes

.. _v3.2.2-backend:

3.2.2 (backend)
===============

* *Release: 20 August 2021*
* **Key changes:**
  
  * Fix questionnaire duplications for admin in list view

.. _v3.2.1-backend:

3.2.1 (backend)
===============

* *Release: 6 August 2021*
* **Key changes:**
  
  * Fix KM package deserialization for Registry

.. _v3.2:

3.2
===

* *Release: 3 August 2021*
* **Key changes:**
  
  * Custom metrics (in KM)
  * Custom phases (in KM)
  * Several optimizations

.. _v3.1:

3.1
===

* *Release: 25 June 2021*
* **Key changes:**
  
  * Project templates
  * Minor UI improvements

.. _v3.0:

3.0
===

* *Release: 1 June 2021*
* **Key changes:**
  
  * Migration from MongoDB and RabbitMQ to PostgreSQL and S3
  * Deep links feature

.. _v2.14:

2.14
====

* *Release: 4 May 2021*
* **Key changes:**
  
  * Submitting forms using Enter key
  * Shortcuts for KM Editor and Forking KM
  * Clarified public link for project in UI

.. _v2.13:

2.13
====

* *Release: 7 April 2021*
* **Key changes:**
  
  * Auto-reconnect in questionnaires (websockets)
  * Fix text inputs in questionnaires when using Grammarly in browser
  * Added actions directly to list views of knowledge models and templates

.. _v2.12:

2.12
====

* *Release: 12 March 2021*
* **Key changes:**
  
  * Questionnaire versioning (Version History)

.. _v2.11:

2.11
====

* *Release: February 2021*
* **Key changes:**
  
  * Add multiple choice question
  * Show tags in the questionnaire

.. _v2.10:

2.10
====

* *Release: January 2021*
* **Key changes:**
  
  * Possibility to add specific users to the questionnaire as collaborators

.. _v2.9:

2.9
===

* *Release: 9 December 2020*
* **Key changes:**
  
  * Refactored error messages
  * Several bugfixes

.. _v2.8.1-backend:

2.8.1 (backend)
===============

* *Release: 24 November 2020*
* **Key changes:**
  
  * Fix version ordering for KM package and templates
  * Fix move question in questionnaire migration
  * Filter out unsupported templates for select
  * Fix available non-latest templates
  * Clear default template after project migration

.. _v2.8:

2.8
===

* *Release: 3 November 2020*
* **Key changes:**
  
  * Pagination & sorting in table views
  * Introduced DSW Template Development Kit
  * Minor UX improvements

.. _v2.7:

2.7
===

* *Release: 5 October 2020*
* **Key changes:**
  
  * Improved caching for speed optimization
  * Reworked questionnaire detail

.. _v2.6:

2.6
===

* *Release: 9 September 2020*
* **Key changes:**
 
  * Added questionnaire live collaboration
  * Introduced Projects to relate questionnaire, TODOs, documents, and settings
  * Several UI/UX improvements
  * Improved design of email templates

.. _v2.5:

2.5
===

* *Release: 8 July 2020*
* **Key changes:**
  
  * Added templates management
  * Several UI/UX improvements
  * Introduced backend workers for scheduled/async tasks
  * Added option to disable questionnaire summary report

.. _v2.4:

2.4
===

* *Release: 3 June 2020*
* **Key changes:**
  
  * Added RDF support step in document worker
  * Improved default naming of new documents
  * Minor UI/UX improvements
  * Several bugfixes

.. _v2.3:

2.3
===

* *Release: 6 May 2020*
* **Key changes:**
  
  * Enhanced backend logging for ELK
  * Added document submission
  * Improved integration with Registry for simpler Sign Up
  * Added user avatars
  * Several bugfixes and optimizations

.. _v2.2:

2.2
===

* *Release: 1 April 2020*
* **Key changes:**
  
  * Added support for OpenID
  * Added affiliations in user profiles
  * Introduced settings to change configurations directly in DSW interface
  * Added API documentation using Swagger
  * UI/UX improvements
  * Several bugfixes and optimizations

.. _v2.1:

2.1
===

* *Release: 3 March 2020*
* **Key changes:**
  
  * Introduced document worker for better scalability
  * Migrated backend to new framework
  * Added dropdown actions to list views
  * Several bugfixes

.. _v2.0:

2.0
===

* *Release: 14 January 2020*
* **Key changes:**
  
  * Added move functionality for knowledge models
  * Added possibility to assign template to KMs
  * Added questionnaire cloning
  * Added expand/collapse all in KM Editor
  * Internal refactoring and structure enhancements
  * Several bugfixes

.. _v1.10.1-frontend:

1.10.1 (frontend)
=================

* *Release: 18 September 2019*
* **Key changes:**
  
  * Knowledge Model Editor UI Fixes
  * Mistyped parameter in DMP macro for indications

.. _v1.10:

1.10
====

* *Release: 3 September 2019*
* **Key changes:**
  
  * Improving client caching
  * Refactor KM to flat structure
  * Add uuids in editor
  * Add helpers for templates
  * Followup questions missing in KM migration
  * Localization
  * Update MongoDB (4.0.12)
  * Switch follow up questions and metrics in the editor
  * Non-ascii characters do not work in the templates
  * Remove itemTitle option
  * Deleting an item in Integration headers doesn't indicate a change
  * Problem with empty integration file
  * Wrong padding for tag selection in preview in KM Editor
  * Chapter text should not be required
  * Use app title in default email template

.. _v1.9.2-backend:

1.9.2 (backend)
===============

* *Release: 13 August 2019*
* **Key changes:**
  
  * Bad defaults for ADMIN role

.. _v1.9.1-backend:

1.9.1 (backend)
===============

* *Release: 7 August 2019*
* **Key changes:**
  
  * Invalid serialization on Typehint endpoint

.. _v1.9:

1.9
===

* *Release: 30 June 2019*xww
* **Key changes:**
  
  * Migrate Questionnaires to new KM Model
  * Add License to Registry
  * Pre-fill last KM package version on deployment
  * Non-desirable questions should not appear in the report
  * Create tags integration tests
  * Wrong computation of Outdated indication in Editor
  * Questionnaire name in the default DMP template
  * Extend DMP Template with information about used KM
  * Custom links in menu
  * Add flags to the questionnaire and questionnaire migration
  * Questionnaire migration integration tests
  * Timestamps for KMs & Questionnaires
  * Allow to set up mail server without authentication
  * "Save" and "Save and close" buttons for KM Editor
  * Case insensitive order in client list views
  * User not logged out when deleted
  * Improve item question in read-only questionnaire
  * Don't show metrics in summary report when no metrics are used

.. _v1.8.1-frontend:

1.8.1 (frontend)
================

* *Release: 13 June 2019*
* **Key changes:**
  
  * Changing accessibility of questionnaire in create or edit form does not work in Safari

.. _v1.8:

1.8
===

* *Release: 13 June 2019*
* **Key changes:**
  
  * Dot notation for integration result objects
  * Integration with BioTools
  * Integration with Tess
  * Create basic questionnaire integration tests
  * Add support for markdown to KM descriptions
  * Integrate Registry into DSW project
  * Option for turning off Questionnaire Accessibility
  * Add privacy URL to the client configuration
  * Fix metamodel migration
  * Wrong logo position in exported PDF DMP
  * Integration props not visible in editor before saving

.. _v1.7:

1.7
===

* *Release: 16 May 2019*
* **Key changes:**
  
  * Create a Dashboard
  * Item Title in List of Items should go away
  * Summary Report Optimization
  * Dynamically configurable client
  * Configurable phases
  * Read only questionnaire
  * Useless feedback button next to item name input
  * Support table actions for touch screens
  * Wrong height of Editor Preview window
  * Inconsistent error page
  * Wrong text at empty Knowledge Models empty state

.. _v1.6:

1.6
===

* *Release: 7 May 2019*
* **Key changes:**
  
  * Multiple server-side configurable DMP templates
  * Automatic metamodel migrations
  * Change visibility of questionnaire doesn't work
  * Typehints
  * DSW-Server build in Travis review & speedup
  * Email inline images compatibility
  * Test editing entities in KM Editor
  * Test Organization module
  * Test Users module
  * Configurable application title
  * Configurable messages on welcome screen
  * Old "Report Issue" GitHub link

.. _v1.5:

1.5
===

* *Release: 9 April 2019*
* **Key changes:**
  
  * Dynamically computed identifier in Questionnaire and DMP
  * Brand client application
  * Questionnaire - chapter list should not scroll with the content
  * Guide user to be more FAIR
  * Indication of not complete questions
  * Upgrade elm/http package
  * Actions when mailer fails to send email
  * Change name and visibility of a questionnaire
  * Make RabbitMQ optional
  * Improve table actions
  * Graphical visualization of report
  * Use configuration file for API URL
  * Reverse-order of Package version list
  * Buttons in package detail versions are too close to text
  * Rename modules and URLs according to the new terminology

.. _v1.4:

1.4
===

* *Release: 10 March 2019*
* **Key changes:**
  
  * Add tags to KM Editor
  * Use tags when creating Questionnaire
  * Knowledge Model cannot be saved when a type of reference is changed
  * Email templates
  * KM Tags Editor view (table)
  * Merge KM Editor & KM Tags Editor into a single view
  * Questionnaire preview in KM Editor
  * Rename Ids to Uuids in entity properties
  * Add version to KM package
  * Refactor question entity structure
  * Mail config options parsed even when disabled

.. _v1.3:

1.3
===

* *Release: 10 February 2019*
* **Key changes:**
  
  * Email should be case insensitive in login form
  * Allow SSL in server's internal SMTP mailer
  * Editable DMP template and style (through static HTML file on server)
  * Include metadata into DMP template

.. _v1.2.1-backend:

1.2.1 (backend)
===============

* *Release: 14 January 2019*
* **Key changes:**
  
  * Distinguish between DB and KM migrations

.. _v1.2:

1.2
===

* *Release: 13 January 2019*
* **Key changes:**

  * Update questionnaire replies structure
  * Editor should open an alert when leaving unsaved knowledge model
  * Retry connect to MongoDB, RabbitMQ when starting the server
  * Split user menu
  * Allow to export and import more KM packages at once
  * Fix user delete modal email overflow

.. _v1.1:

1.1
===

* *Release: 16 December 2018*
* **Key changes:**
  
  * Bug in KM Editor: Item Title does not change
  * Add endpoint for uploading KMPs
  * Convert all book references from HTML to Markdown
  * Add new logo to the client
  * Summary report doesn't work as expected
  * After the questionnaire is created, user should be redirect to the questionnaire
  * Save which user has created a Knowledge Model
  * Data Steward should be able to export and import KM packages
  * DS Planner List - display whether the questionnaire is public or private
  * Data Steward and Researcher can't edit / delete other public questionnaires
  * RabbitMQ
  * Unify the terminology
  * Questionnaire - Phase Select - it breaks to multiple lines on smaller screens
  * Save which user has created Questionnaire
  * Table actions should have unbreakable space if the action name has more words
  * Create Favicon

.. _v1.0:

1.0
===

* *Release: 30 October 2018*

# New features and improvements

List any new features and improvements made here.

# Breaking changes

List any breaking changes here, along with a brief reason why they were made (eg to add a new feature).

# Migration

If any breaking changes were made, list how to handle them here.

# Bug fixes

List any bug fixes made here.

# Related issue

Closes #{{issue.iid}}

# Definition of Done

## All developments
- [ ] Feature was implemented as per the requirements
- [ ] If some code parts are complex they must be commented with code documentation
- [ ] If feature affects the corresponding Governance Policy, then the policy has been updated and a new version of the policy set up (before the template is QA tested)
- [ ] QA tests are successful (please comment with a link to the created component & tested DP)
    - Template must be tested by:
        - Creating a component with it in QA env
        - Committing the DP
        - Launching a test on the DP in the Control Panel
        - Deploying the DP
            - Mocked components are acceptable: eg for a template of a Spark workload we do not need to actually implement business logic. We don't need to actually develop on the component for every single feature.
- [ ] Documentations have been updated
    - Both the documentation of the template, and the documentation of the component inside the skeleton, must be updated (if one, the other or both of course depends on the kind of work we're doing)
    - Documentation has been updated with explanation of the new feature if it is user-facing (eg component now has additional setting) or it impacts him in some other way (eg optional field that becomes mandatory)
    - If it is a breaking change we have documented them as such in the MR description in a "Breaking Changes" section

## Wizard development
- [ ] The wizard design has been implemented according to the provided wireframes, mockups, or design specifications
- [ ] The UI elements are visually consistent, aesthetically pleasing, and aligned with the brand guidelines
- [ ] Dynamic elements, such as dropdowns, sliders, and modals, function as expected and enhance the user experience. Also edge conditions have been tested
- [ ]  Labels everywhere are meaningful to the user. All labels have been reviewed
- [ ] Embedded images use sensible hosting strategy
- [ ] The wizard steps are clear to the users

## Skeleton/component template development
- [ ] If feature affects the skeleton of a component that contains a codebase (eg introducing new feature in the codebase), unit tests for that feature are added to the codebase


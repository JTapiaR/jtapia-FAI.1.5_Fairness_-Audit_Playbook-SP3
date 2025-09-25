import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
from sklearn.metrics import accuracy_score
from fairlearn.metrics import MetricFrame

# --- Page Configuration ---
st.set_page_config(
    layout="wide",
    page_title="Fairness Implementation Playbook",
    page_icon="📘"
)
# --- App Header ---
st.header("Fairness Implementation Playbook 📘")
st.info("A comprehensive methodology for deploying fairness solutions across AI systems and organizations by bridging technical solutions with organizational realities.")

st.subheader("👩‍💻 Developer's Guide to the Fairness Implementation Framework")
st.write("Click the link below to open the developer's guide in a new tab.")
documentation_url = "https://laboratoriodeiaparanosotras.my.canva.site/guide-to-navigating-the-fairness-implementation-playbook"
st.markdown(f"""
<a href="{documentation_url}" target="_blank">
    Developer's Guide to the Fairness Implementation Framework
</a>
""", unsafe_allow_html=True)

st.info("The link will open in a new browser tab.")


# --- Main Tabs for the Playbook Structure ---
part1, part2, part3, part4, part5 = st.tabs([
    "**Part 1: Fair AI Scrum Toolkit**",
    "**Part 2: Organizational Integration Toolkit**",
    "**Part 3: Advanced Architecture Cookbook**",
    "**Part 4: Regulatory Compliance & Risk Alignment**",
    "**Part 5: Full Playbook & Synthesis**"
])

# --- PART 1: FAIR AI SCRUM TOOLKIT ---
with part1:
    st.header("Part 1: Fair AI Scrum Toolkit")
    st.info(
        "**Objective:** To embed fairness within individual agile teams by redesigning Scrum artifacts, creating fairness-aware user stories, establishing a robust 'Definition of Done', and adapting ceremonies for fairness discussions. This toolkit provides the foundational, team-level practices for building equitable AI systems."
    )

    st.markdown("---")

    # --- 1. User Documentation: How to Apply This Toolkit ---
    st.subheader("🚀 How to Apply This Toolkit: A 5-Step Guide")
    st.markdown("Use this framework to systematically integrate fairness into your team's existing Scrum process.")

    cols = st.columns(5)
    with cols[0]:
        st.markdown("##### 1. Assess")
        with st.popover("Details"):
            st.markdown("""
            **Goal:** Document your team's current Scrum implementation to identify gaps where fairness can be integrated.
            
            **Action Items:**
            - Review your user story templates. Do they mention user impact or only functionality?
            - Check your Definition of Done. Does it include any form of bias or fairness validation?
            - Listen during standups and retrospectives. Is fairness ever discussed?
            """)

    with cols[1]:
        st.markdown("##### 2. Modify Artifacts")
        with st.popover("Details"):
            st.markdown("""
            **Goal:** Enhance core Scrum artifacts to make fairness a formal requirement, not an afterthought.
            
            **Action Items:**
            - Update user story templates to include fairness goals and protected groups.
            - Add fairness validation criteria to your team's Definition of Done.
            - Create specific task templates in your backlog for fairness work (e.g., "Audit dataset for bias").
            """)
    
    with cols[2]:
        st.markdown("##### 3. Redesign Ceremonies")
        with st.popover("Details"):
            st.markdown("""
            **Goal:** Create explicit touchpoints for fairness discussions in every Scrum ceremony.
            
            **Action Items:**
            - Add "Fairness Risk Assessment" to your sprint planning agenda.
            - Modify the daily standup to include reporting on "fairness blockers".
            - Require fairness metrics to be shown in sprint reviews.
            - Add fairness-focused questions to your retrospective templates.
            """)

    with cols[3]:
        st.markdown("##### 4. Clarify Roles")
        with st.popover("Details"):
            st.markdown("""
            **Goal:** Distribute fairness accountability across the entire team to prevent diffusion of responsibility.
            
            **Action Items:**
            - Formally extend the definitions of Product Owner, Scrum Master, and Developer roles to include specific fairness responsibilities.
            - Create a simple RACI matrix for key fairness tasks like bias auditing and mitigation planning.
            """)

    with cols[4]:
        st.markdown("##### 5. Pilot & Iterate")
        with st.popover("Details"):
            st.markdown("""
            **Goal:** Test the changes, gather feedback, and refine your approach gradually.
            
            **Action Items:**
            - Pilot the new toolkit for one or two sprints.
            - Use the retrospective to gather feedback on what worked and what didn't.
            - Frame the changes as enhancing product quality to get stakeholder buy-in.
            """)

    st.markdown("---")

    # --- 2. Scrum Artifact Modification Guide ---
    st.subheader("📝 Scrum Artifact Modification Guide")
    st.markdown("Traditional Scrum artifacts capture functional requirements but often ignore fairness dimensions, creating a gap where bias can slip through undetected. This guide shows you how to modify them.")

    tab_stories, tab_backlog, tab_dod = st.tabs(["User Stories", "Sprint Backlog", "Definition of Done (DoD)"])

    with tab_stories:
        st.markdown("##### Integrating Fairness into User Stories")
        st.markdown("The user story is the starting point for development. Modifying it forces the team to consider fairness from the very beginning.")
        
        col1, col2 = st.columns(2)
        with col1:
            st.error("**Traditional Story (Fairness-Blind)**")
            st.markdown("Focuses exclusively on functional needs.")
            st.code("""
As a recruiter,
I want to filter candidates by level of experience,
So I can focus on qualified applicants.
            """, language="markdown")
        
        with col2:
            st.success("**Modified Story (Fairness-Aware)**")
            st.markdown("Adds an explicit, measurable fairness goal.")
            st.code("""
As a recruiter,
I want to filter candidates by level of experience,
So I can focus on qualified applicants,
WHILE ENSURING equivalent filtering accuracy across gender and age groups.
            """, language="markdown")

    with tab_backlog:
        st.markdown("##### Integrating Fairness into the Sprint Backlog")
        st.markdown("A user story with a fairness requirement must lead to specific fairness tasks in the backlog. This ensures that time and resources are allocated for the work.")

    with tab_dod:
        st.markdown("##### Integrating Fairness into the Definition of Done (DoD)")
        st.markdown("The DoD acts as the final quality gate. Including fairness validation makes it a non-negotiable requirement for completion, preventing biased systems from reaching production. A fairness-aware DoD is the mechanism that verifies if the fairness goal from the user story was achieved.")
        st.warning("A DoD that ignores fairness sends a message that bias validation is less important than other quality aspects.")
        st.markdown("See the **Definition of Done Framework** section below for a detailed checklist.")

    st.markdown("---")

    # --- 3. Fairness User Story Template Library ---
    st.subheader("📚 Fairness User Story Template Library")
    st.markdown("Use this template to translate abstract fairness concepts into actionable development tasks.")

    st.success("""
    **Template:** `As a` **[Persona]**, `I want to` **[Action]**, `so that` **[Benefit]**, `while ensuring` **[Fairness Goal]** `for` **[Protected and Intersectional Groups]**.
    """)

    with st.expander("View Examples for Common AI Scenarios"):
        st.markdown("##### Example 1: AI Recruitment")
        st.code("""
As a hiring manager,
I want to use an AI model to screen resumes for relevant skills,
So I can identify top candidates efficiently,
WHILE ENSURING the screening accuracy is equivalent across racial and gender groups, paying special attention to intersectional groups like women of color.
        """, language="markdown")
        st.markdown("This addresses the need to consider intersectional impacts, not just single attributes.")

        st.markdown("##### Example 2: Loan Approval System")
        st.code("""
As a loan officer,
I want to use a model to predict the likelihood of loan default,
So I can make faster and more consistent approval decisions,
WHILE ENSURING the false rejection rate (declining a qualified applicant) is balanced across different age brackets and geographic locations (zip codes).
        """, language="markdown")

        st.markdown("##### Example 3: Content Moderation")
        st.code("""
As a platform administrator,
I want to use a model to automatically flag harmful content,
So I can maintain a safe online environment,
WHILE ENSURING the model's false positive rate for flagging content as harmful is equitable across dialects and sociolects present in user-generated text.
        """, language="markdown")

    st.markdown("---")

    # --- 4. Definition of Done (DoD) Framework ---
    st.subheader("✅ Definition of Done (DoD) Framework")
    st.markdown("This framework extends a standard DoD to include mandatory fairness validation, creating a systematic checkpoint to prevent biased systems from being deployed.")

    st.markdown("A feature is **Done** only when all the following criteria are met:")
    
    st.info("##### Functional & Quality Criteria (Standard)")
    st.checkbox("Code is peer-reviewed and merged.", value=True, disabled=True, key="dod_c1")
    st.checkbox("Unit and integration tests pass.", value=True, disabled=True, key="dod_c2")
    st.checkbox("Feature meets functional acceptance criteria.", value=True, disabled=True, key="dod_c3")
    st.checkbox("Documentation is updated.", value=True, disabled=True, key="dod_c4")
    
    st.success("##### Fairness Validation Criteria (Extended)")
    st.checkbox("**Bias tests for identified protected groups have been executed and the results are documented.**", key="dod_f1")
    st.checkbox("**Fairness metrics (e.g., demographic parity, equal opportunity) meet the pre-defined thresholds from the user story's acceptance criteria.**", key="dod_f2")
    st.checkbox("**Performance has been evaluated with disaggregated testing across key intersectional subgroups (e.g., older women, younger men).**", key="dod_f3")
    st.checkbox("**A review of potential negative downstream impacts has been conducted and documented.**", key="dod_f4")

    st.markdown("---")

    # --- 5. Ceremony Adaptation Guide ---
    st.subheader("💬 Ceremony Adaptation Guide")
    st.markdown("Modify each Scrum ceremony to include dedicated fairness checkpoints. This ensures fairness is discussed proactively and consistently, rather than reactively when it's too late.")

    planning_expander, standup_expander, review_expander, retro_expander = st.columns(4)

    with planning_expander:
        with st.expander("**Sprint Planning**", expanded=True):
            st.markdown("##### Goal: Evaluate risks and allocate resources upfront.")
            st.markdown("""
            - **Agenda Item:** Explicitly discuss fairness risks and potential impacts of the stories in the upcoming sprint.
            - **Resource Allocation:** Justify decisions to allocate a portion of the sprint's capacity (e.g., 20%) to fairness-specific work like auditing, bias testing, or mitigation.
            - **Role of Product Owner:** The PO leads the discussion on fairness risks and priorities.
            """)

    with standup_expander:
        with st.expander("**Daily Standup**", expanded=True):
            st.markdown("##### Goal: Make fairness a daily, tangible concern.")
            st.markdown("""
            - **Key Change:** Add a fourth question or integrate into the "blockers" discussion: "**Are there any fairness blockers?**".
            - **Example Blockers:**
                - *"I can't validate the impact on an intersectional group because we lack sufficient labeled data."*
                - *"I'm not sure how to interpret the results of this fairness metric for our user story."*
            - **Role of Scrum Master:** The SM's role is extended to actively track and help remove these fairness blockers.
            """)

    with review_expander:
        with st.expander("**Sprint Review**", expanded=True):
            st.markdown("##### Goal: Demonstrate fairness outcomes, not just features.")
            st.markdown("""
            - **Demonstration:** When demonstrating a new feature, the team must also present the fairness metrics and the results of disaggregated testing.
            - **Shift in Focus:** This changes the definition of a "successful" demo from just "it works" to "it works *and* it's fair."
            - **Example:**
            """)
            st.code("""
# Example of a simple metric check to show in a review
def check_demographic_parity(predictions, sensitive_attributes):
    # This is a simplified example
    group_a_approval_rate = ...
    group_b_approval_rate = ...
    disparity = abs(group_a_approval_rate - group_b_approval_rate)
    
    st.metric(
        label="Demographic Parity Disparity", 
        value=f"{disparity:.2%}", 
        delta="-1.2%",  # Compared to last sprint
        help="Lower is better. Measures if all groups have a similar approval rate."
    )
    return disparity < 0.1 # Threshold from acceptance criteria
            """, language="python")

    with retro_expander:
        with st.expander("**Retrospective**", expanded=True):
            st.markdown("##### Goal: Improve the process for building fair AI.")
            st.markdown("""
            - **Expand Criteria for Success:** Move beyond only discussing velocity and technical debt to include reflections on fairness outcomes.
            - **New Questions to Ask:**
                - *"Did we have the right data and tools to address fairness in this sprint?"*
                - *"Did we create a psychologically safe environment to discuss bias openly?"*
                - *"Have we improved our ability to create a fairer product in this sprint?"*
            """)

    st.markdown("---")

    # --- 6. Case Study: AI Resume Screening System ---
    st.subheader(" Case Study: AI-Based Resume Screening System")
    st.markdown("This case study demonstrates the toolkit's application to a real-world scenario.")

    case_context, case_problem, case_solution = st.tabs(["Scenario Context", "The Problem (Without the Toolkit)", "The Solution (With the Toolkit)"])

    with case_context:
        st.markdown("""
        **Application Domain:** Human Resources & Recruitment.
        **ML Task:** A classification model to predict whether a candidate's resume is a good match for a specific job description.
        **Stakeholders:** Recruiters, hiring managers, candidates, and the development team.
        **Fairness Challenge:** Initial prototypes show the system favors candidates from specific universities and penalizes applicants with non-traditional career paths or resume formats, which is correlated with socioeconomic and racial background.
        """)

    with case_problem:
        st.markdown("""
        The team initially followed a standard Scrum process, leading to critical failures:
        1.  **Artifact Gap:** User stories were purely functional, like *"As a recruiter, I want to see a candidate's 'match score'"*. This led developers to optimize for predictive accuracy alone, perpetuating the biases in the historical data.
        2.  **Ceremony Gap:** Sprint reviews only showed aggregate accuracy metrics (e.g., "90% accuracy"), which masked poor performance for minority subgroups. The issue wasn't discovered until late in development.
        3.  **Role Confusion & Responsibility Gap:** No one owned the fairness outcome.
            - The **Product Owner** prioritized features that increased recruiter efficiency over tasks to fix fairness issues.
            - **Developers** assumed fairness was someone else's problem to be handled "later".
            - The **Scrum Master** saw discussions about bias as "conflict" to be avoided rather than a productive part of the process.
        
        **Result:** A system that was technically functional but discriminatory, created by a team with good intentions but a flawed process.
        """)
    
    with case_solution:
        st.markdown("The team pilots the **Fair AI Scrum Toolkit** for two sprints. Here’s how it changes their process:")
        
        st.info("##### 1. Modified User Story")
        st.markdown("The Product Owner, now responsible for prioritizing fairness, reframes the central user story:")
        st.code("""
As a recruiter,
I want to see a candidate's 'match score',
So I can quickly identify promising applicants,
WHILE ENSURING the model provides an equal opportunity for selection across gender and racial groups (i.e., achieves a similar true positive rate for all groups).
        """, language="markdown")

        st.info("##### 2. Adapted Sprint Planning & Backlog")
        st.markdown("During Sprint Planning, the team discusses the risk of bias from training data. They allocate **20% of their sprint capacity** to fairness tasks, which are added to the backlog:")
        st.markdown("""
        - **Fairness Task 1:** Audit training data for representation of different demographic groups.
        - **Fairness Task 2:** Implement the 'Equal Opportunity' fairness metric as a test.
        - **Fairness Task 3:** Research and experiment with one bias mitigation algorithm (e.g., reweighing).
        """)

        st.info("##### 3. New Daily Standup Dynamic")
        st.markdown("A developer raises a **fairness blocker**:")
        st.markdown("> *\"I'm blocked on implementing the Equal Opportunity test because our dataset lacks reliable demographic labels for a key subgroup. I can't proceed without this data.\"*")
        st.markdown("The **Scrum Master**, now responsible for removing fairness blockers, immediately works with the Product Owner to find a data source or a proxy solution.")

        st.info("##### 4. Robust Definition of Done")
        st.markdown("Before the feature can be considered 'Done,' the developers, who are now responsible for implementing fairness tests, must prove it passes the new DoD criteria:")
        st.markdown("""
        - ✅ **Bias Test Executed:** They run the Equal Opportunity test.
        - ✅ **Metric Threshold Met:** The difference in the true positive rate between groups is below the 5% threshold defined in the acceptance criteria.
        - ✅ **Disaggregated Testing:** They show results broken down by `gender`, `race`, and `gender+race` to check for intersectional issues.
        """)

        st.info("##### 5. Impactful Sprint Review & Retrospective")
        st.markdown("""
        - **In the Review**, the team demonstrates the resume screener and proudly presents a dashboard showing not just accuracy, but also the fairness metrics that meet their goals.
        - **In the Retrospective**, they discuss how the process felt. A developer notes, *"It was hard at first, but for the first time, I feel like we have a concrete process to build a product that doesn't cause harm."*
        """)
        
        st.success("**Result:** By using the toolkit, the team transforms fairness from a vague ideal into a concrete, trackable, and shared responsibility, leading to a more equitable product.")

    st.markdown("---")

    # --- 7. Bibliography and Further Reading ---
    st.subheader("📚 Further Reading & Bibliography")
    with st.expander("Expand to see key resources for the Fair AI Scrum Toolkit"):
        st.markdown("""
        The concepts in this toolkit are grounded in extensive research on the practical challenges of implementing fairness in real-world AI development. Use these references to deepen your understanding and find evidence to support the adoption of these practices in your organization.

        ##### Foundational Readings:

        - **Holstein, K., et al. (2019). *Improving fairness in machine learning systems: What do industry practitioners need?***
          - **Why it's important:** This is a key paper that identifies the gap between academic fairness research and the needs of industry teams. It highlights the demand for practical tools, checklists, and process integrations, which directly motivates the creation of this toolkit. Use it to understand the "why" behind these tools.
        
        - **Madaio, M. A., et al. (2020). *Co-designing checklists to understand organizational challenges and opportunities around fairness in AI.***
          - **Why it's important:** This research explores how tools like checklists can help teams operationalize fairness. It shows that distributing responsibility and creating concrete tasks (like those in the DoD and user story templates) leads to better outcomes.
        
        - **Vethman, S., et al. (2025). *Fairness beyond the Algorithmic Frame: Actionable Recommendations for an Intersectional Approach.***
          - **Why it's important:** This paper provides the theoretical and practical grounding for the toolkit's emphasis on intersectionality, psychological safety in ceremonies, and interdisciplinary collaboration. It argues for moving beyond purely technical metrics, a core principle of the Fair AI Scrum approach.
          
        ##### On Specific Toolkit Components:

        - **For User Stories & DoD:** **Raji, I. D., et al. (2020). *Closing the AI accountability gap: Defining an end-to-end framework for internal algorithmic auditing.***
          - **Why it's important:** This paper outlines a comprehensive framework for AI auditing, emphasizing the need for clear documentation and validation at each stage of the development lifecycle. The "Definition of Done" and fairness-aware user stories are practical implementations of these principles.
        
        - **For Role Responsibilities:** **Rakova, B., et al. (2021). *Where responsible AI meets reality: Practitioner perspectives on enablers for shifting organizational practices.***
          - **Why it's important:** This work discusses the organizational and cultural shifts needed to make responsible AI a reality. It supports the idea of clarifying roles to ensure fairness doesn't become a "diffusion of responsibility" problem.

        - **For Intersectional Thinking:** **Crenshaw, K. (1989). *Demarginalizing the intersection of race and sex: A black feminist critique...***
          - **Why it's important:** The foundational text on intersectionality. While not about AI, it provides the critical lens for understanding why analyzing fairness across single attributes (e.g., just race or just gender) is insufficient and can hide the most severe forms of bias.
        """)


# --- PART 2: ORGANIZATIONAL INTEGRATION TOOLKIT (GOVERNANCE) ---
with part2:
    st.header("Part 2: Organizational Integration Toolkit 🏛️")
    st.info(
        "**Objective:** To establish governance frameworks that embed fairness accountability throughout your organization. This moves beyond individual team practices to ensure consistent, scalable, and defensible fairness implementation across all AI systems."
    )
    st.markdown("---")

    # --- Main Tabs for Part 2 ---
    (
        tab_guide,
        tab_roles,
        tab_responsibility,
        tab_documentation,
        tab_monitoring,
        tab_case_study,
    ) = st.tabs([
        "**🚀 How to Implement**",
        "**♟️ Strategic Rationale & Roles**",
        "**🗺️ Responsibility & Decisions**",
        "**📄 Documentation & Accountability**",
        "**📊 Dashboards & Monitoring**",
        "**🏢 Case Study**"
    ])

    # --- TAB 1: HOW TO IMPLEMENT ---
    with tab_guide:
        st.subheader("How to Implement This Toolkit: A 5-Step Process")
        st.markdown("Follow these steps to build a robust fairness governance structure within your organization.")
        
        cols = st.columns(5)
        with cols[0]:
            st.markdown("##### 1. Form Governance Body")
            with st.popover("Details"):
                st.markdown("""
                **Goal:** Create a central, cross-functional body with the authority to oversee AI fairness.
                
                **Action Items:**
                - Charter an **AI Review Board** or **AI Ethics Council**.
                - Ensure representation from Legal, Compliance, Product, Engineering, UX, and relevant business units.
                - Grant this body the authority to set policies, review high-risk projects, and make binding decisions.
                """)

        with cols[1]:
            st.markdown("##### 2. Define Key Roles")
            with st.popover("Details"):
                st.markdown("""
                **Goal:** Establish clear fairness-focused roles to operationalize governance.
                
                **Action Items:**
                - Identify and train **Fairness Champions**—subject matter experts who can guide and support individual teams.
                - Formally recognize the **AI Review Board** as the highest authority on fairness decisions.
                - Ensure Product Owners and Managers are formally designated as **accountable** for the fairness outcomes of their products.
                """)
        
        with cols[2]:
            st.markdown("##### 3. Map Responsibilities")
            with st.popover("Details"):
                st.markdown("""
                **Goal:** Eliminate ambiguity by clearly mapping fairness tasks to roles and functions using a responsibility matrix.
                
                **Action Items:**
                - Use the **RASCI Matrix Template** provided in this toolkit.
                - Convene stakeholders from different departments to agree on their roles (Responsible, Accountable, Supportive, Consulted, Informed) for each key fairness task.
                - Publish the matrix as part of your internal AI development policy.
                """)

        with cols[3]:
            st.markdown("##### 4. Standardize Documentation")
            with st.popover("Details"):
                st.markdown("""
                **Goal:** Create a consistent and auditable trail of fairness-related decisions and trade-offs.
                
                **Action Items:**
                - Mandate the use of a **Fairness Impact Statement** and **Model Cards** for all high-risk AI projects.
                - Use the provided templates to document risks, metrics, mitigation efforts, and decision rationales.
                - Store these documents in a central repository for easy access during audits or reviews.
                """)

        with cols[4]:
            st.markdown("##### 5. Establish Escalation Paths")
            with st.popover("Details"):
                st.markdown("""
                **Goal:** Create a clear, efficient process for resolving fairness conflicts and issues.
                
                **Action Items:**
                - Document a formal escalation pathway from the development team up to the AI Review Board.
                - Define clear criteria for what constitutes a high-risk issue that requires escalation (e.g., significant metric disparities, potential legal exposure, unresolved team disagreements).
                """)

    # --- TAB 2: STRATEGIC RATIONALE & ROLES ---
    with tab_roles:
        st.subheader("Strategic Rationale: Why Formal Roles Matter")
        st.markdown("Fairness leadership roles establish dedicated positions with explicit fairness mandates, authority, and resources. They transform fairness from an abstract goal into an operational responsibility.")

        with st.expander("Key Fairness Leadership Roles"):
            st.markdown("""
            - **Chief AI Ethics Officer:** Executive responsible for organization-wide fairness strategy and accountability.
            - **Fairness Program Manager:** Coordinates fairness implementation across teams and products.
            - **Fairness Domain Specialists:** Provide expertise in specific application areas (e.g., hiring, lending).
            - **Technical Fairness Leads:** Oversee fairness implementation within engineering organizations.
            """)

        st.subheader("Organizational Fairness Models")
        st.markdown("Organizations must choose between centralizing fairness expertise or embedding it across teams. **Hybrid models** are often the most effective, balancing deep expertise with broad ownership.")

        model_c, model_e, model_h = st.tabs(["Centralized Model", "Embedded Model", "Hybrid Models (Recommended)"])
        
        with model_c:
            st.markdown("**Description:** A single, specialized team is responsible for all fairness work.")
            st.success("**Pros:** Builds deep, concentrated expertise.")
            st.error("**Cons:** Creates bottlenecks and can lead to a lack of ownership in other teams.")
        
        with model_e:
            st.markdown("**Description:** Fairness responsibilities are distributed across all development teams.")
            st.success("**Pros:** Fosters broad ownership and awareness.")
            st.error("**Cons:** Dilutes expertise and can lead to inconsistent standards.")

        with model_h:
            st.markdown("Hybrid models combine centralized expertise with embedded ownership. Research by Holstein et al. (2019) found these models achieved **43% higher implementation rates** than purely centralized models.")
            st.markdown("##### Common Hybrid Models:")
            st.markdown("- **Center of Excellence Model:** Central team develops standards and tools; embedded champions implement them.")
            st.markdown("- **Hub and Spoke Model:** A core 'hub' team provides leadership while designated 'spokes' (specialists) operate within business units.")
            st.markdown("- **Federated Governance Model:** Business units have primary responsibility, with a central body ensuring consistency.")

        with st.expander("🌍 Intersectional Considerations for Roles"):
            st.markdown("""
            To effectively address intersectional fairness, it's crucial to go beyond technical roles and integrate diverse perspectives into governance itself. As Vethman et al. (2025) note, a "fear of not knowing enough" can make teams hesitant to apply an intersectional framework. A well-designed governance structure mitigates this fear.
            
            **Recommendations:**
            - **Diverse Leadership:** Include people with intersectional lived experiences in fairness leadership positions.
            - **Diverse Governance Bodies:** Create councils where multiple identities and perspectives exist to avoid groupthink.
            - **Explicit Responsibility:** Clearly define responsibility for intersectional analysis in your RACI matrix.
            """)

    # --- TAB 3: RESPONSIBILITY & DECISIONS ---
    with tab_responsibility:
        st.subheader("Responsibility Assignment Matrix (RASCI)")
        st.markdown("Use this matrix to clarify who does what for key fairness tasks. **R**esponsible, **A**ccountable, **S**upportive, **C**onsulted, **I**nformed.")
        
        rasci_data = {
            'Fairness Task': [
                "Define Fairness Metrics for a Project", 
                "Conduct Fairness Audit & Bias Testing", 
                "Approve Bias Mitigation Strategy", 
                "Document Fairness Decisions & Trade-offs", 
                "Handle Post-Deployment Fairness Incident"
            ],
            'AI Dev Team (Data Scientist/Dev)': ["R", "R", "S", "R", "R"],
            'Product Owner': ["A", "A", "A", "A", "A"],
            'Fairness Champion': ["C", "S", "C", "S", "S"],
            'Legal & Compliance': ["C", "I", "C", "I", "C"],
            'AI Review Board': ["I", "I", "A (for high-risk)", "I", "A"]
        }
        df_rasci = pd.DataFrame(rasci_data)
        st.dataframe(df_rasci, hide_index=True)
        with st.expander("How to read this RASCI Matrix"):
            st.markdown("""
            - **Responsible (R):** The person(s) who does the work.
            - **Accountable (A):** The person who ultimately owns the outcome. There should only be one 'A' per task.
            - **Supportive (S):** Provides resources or assistance to the Responsible party.
            - **Consulted (C):** Provides input and expertise. Communication is two-way.
            - **Informed (I):** Kept up-to-date on progress. Communication is one-way.
            """)
        
        st.subheader("Decision Tiers & Escalation Procedures")
        st.markdown("Establish multiple levels for fairness decisions with clear escalation paths to prevent ambiguity and delays.")

        with st.expander("Tier 1: Operational Decisions (Team Level)"):
            st.markdown("**Examples:** Implementation details, monitoring parameters, technical adjustments.")
            st.markdown("**Authority:** Team Leads, Technical Specialists.")
        
        with st.expander("Tier 2: Tactical Decisions (Department Level)"):
            st.markdown("**Examples:** Fairness metric selection for a project, approval of mitigation approaches, threshold adjustments.")
            st.markdown("**Authority:** Department Leadership, Fairness Program Leads.")

        with st.expander("Tier 3: Strategic Decisions (Organizational Level)"):
            st.markdown("**Examples:** Selection of the company-wide fairness framework, policy-level trade-offs, inclusion of new protected attributes.")
            st.markdown("**Authority:** Executive Leadership, AI Review Board.")
        
        st.subheader("Governance Gates for Fairness")
        st.markdown("Implement explicit checkpoints where fairness properties must be formally verified before a project can proceed.")

        st.info("Interactive Gate Check Simulation")
        gate1 = st.checkbox("Data Review Gate: Training data properties and biases documented.", key="p2_g1")
        gate2 = st.checkbox("Design Approval Gate: Fairness implications of model architecture evaluated.", key="p2_g2")
        gate3 = st.checkbox("Pre-Deployment Gate: Fairness metrics validated and meet thresholds.", key="p2_g3")
        gate4 = st.checkbox("Monitoring Trigger Gate: Post-deployment monitoring and alert system is active.", key="p2_g4")

        if all([gate1, gate2, gate3, gate4]):
            st.success("All governance gates passed. The project is cleared for deployment.")
        else:
            st.warning("Project cannot proceed until all governance gates are passed.")

    # --- TAB 4: DOCUMENTATION & ACCOUNTABILITY ---
    with tab_documentation:
        st.subheader("Model Cards & Fairness Decision Records (FDRs)")
        st.markdown("Enhance standard documentation to transparently communicate fairness properties, limitations, and key decisions, following frameworks like those proposed by Mitchell et al. (2019).")

        with st.expander("🌍 Intersectional Considerations for Documentation"):
            st.markdown("""
            Traditional documentation often analyzes protected attributes in isolation. An intersectional approach, as advocated by Crenshaw (1989), requires moving beyond this.
            - **Require Disaggregated Reporting:** Mandate that performance metrics are broken down by intersectional subgroups (e.g., older women), not just by 'age' and 'gender' separately.
            - **Acknowledge Gaps:** If intersectional analysis was not possible due to data limitations, this must be explicitly stated as a limitation in the model card.
            """)

        st.markdown("##### Enhanced Model Card Template")
        st.markdown("A Model Card provides essential details about a model's performance and limitations. The template below adds an explicit **Fairness & Intersectional Analysis** section.")
        
        model_card_template = """
### Model Details
- **Model developer:** AI Dev Team Alpha
- **Model date:** 2025-09-25
- **Model version:** v2.1

### Intended Use
- **Primary use:** To screen resumes and provide a 'match score' for job requisitions.
- **Out-of-scope uses:** Not to be used for final hiring decisions without human review.

### Training Data
- **Source:** Internal historical application data from 2020-2024.
- **Key Demographics:** Analysis performed on gender and race subgroups. *Limitation: Data for non-binary individuals was insufficient for robust analysis.*

### Evaluation Data
- **Dataset:** Stratified sample of 5,000 applications from Q1 2025.
- **Demographics:** Gender, Race, Age Bracket.

## Fairness & Intersectional Analysis
- **Fairness Metrics:** Equal Opportunity (True Positive Rate Parity).
- **Groups Analyzed:** Gender, Race, Age Bracket, and intersections (e.g., 'Women, Age 40+').
- **Findings:** The model achieves Equal Opportunity with a TPR difference of <3% for individual attributes.
- **Intersectional Gaps:** A performance gap was found for 'Women, Age 40+', whose TPR was 7% lower than the baseline.
- **Mitigation:** A post-processing threshold adjustment was applied specifically for this subgroup.

## Ethical Considerations
- **Risks:** Risk of reinforcing historical hiring patterns.
- **Mitigations:** Human-in-the-loop review required for all candidates in underrepresented groups.
        """
        st.code(model_card_template, language="markdown")
        st.download_button(label="Download Model Card Template", data=model_card_template, file_name="Model_Card_Template.md")

    # --- TAB 5: DASHBOARDS & MONITORING ---
    with tab_monitoring:
        st.subheader("Metric Dashboards & Monitoring Systems")
        st.markdown("Effective fairness dashboards translate complex metrics into actionable insights for different audiences and integrate with governance to trigger responses.")

        with st.expander("Dashboard Design Principles"):
            st.markdown("A good dashboard adapts its content to its audience, provides context, and is organized hierarchically.")
            d_exec, d_mgmt, d_tech = st.tabs(["Executive View", "Management View", "Technical View"])
            with d_exec:
                st.markdown("**Focus:** High-level fairness health and risk indicators.")
                st.metric("Overall Fairness Risk Score", "Medium", delta="-3%", help="Change from last quarter.")
            with d_mgmt:
                st.markdown("**Focus:** System-level fairness with comparative context and trends.")
            with d_tech:
                st.markdown("**Focus:** Detailed, disaggregated metrics with statistical rigor (e.g., confidence intervals).")

        with st.expander("Disaggregation and Intersectionality in Dashboards"):
            st.markdown("Aggregate metrics hide bias. Effective dashboards must allow users to **disaggregate** data and analyze **intersectional** performance.")
            st.info("💡 Interactive Example: Intersectional Performance Heatmap")
            
            # Mock data for heatmap
            heatmap_data = pd.DataFrame({
                'Gender': ['Men', 'Men', 'Women', 'Women', 'Non-Binary', 'Non-Binary'],
                'Race': ['Group A', 'Group B', 'Group A', 'Group B', 'Group A', 'Group B'],
                'Accuracy': [0.92, 0.91, 0.90, 0.82, 0.85, 0.79] # Notice the low score for Women, Group B
            })
            
            heatmap_chart = alt.Chart(heatmap_data).mark_rect().encode(
                x='Gender:N',
                y='Race:N',
                color=alt.Color('Accuracy:Q', scale=alt.Scale(scheme='redyellowgreen')),
                tooltip=['Gender', 'Race', 'Accuracy']
            ).properties(
                title='Model Accuracy Across Intersectional Groups'
            )
            st.altair_chart(heatmap_chart, use_container_width=True)
            st.error("The heatmap immediately reveals a critical fairness issue for **Women in Group B** that would be hidden in an overall accuracy score.")

        with st.expander("Monitoring Systems and Alert Frameworks"):
            st.markdown("""
            - **Fairness Drift Detection:** Track statistical changes in fairness metrics over time, not just static values.
            - **Tiered Alert Framework:** Define different severity levels (e.g., 'Warning', 'Critical') and response protocols for fairness metric violations.
            - **Governance Integration:** Alerts should automatically trigger governance processes. A 'Critical' alert might require an immediate review by the **AI Review Board**.
            """)

    # --- TAB 6: CASE STUDY ---
    with tab_case_study:
        st.subheader("Case Study: Multi-Team AI Recruitment Platform")
        st.markdown("This case study shows how governance prevents chaos when multiple teams collaborate on a complex AI system.")

        case_context, case_problem, case_solution = st.tabs(["Scenario Context", "The Problem (Without Governance)", "The Solution (With Governance)"])

        with case_context:
            st.markdown("""
            **System:** A comprehensive AI recruitment platform.
            - **Team A (Sourcing):** Builds a resume screening model.
            - **Team B (Matching):** Builds a recommendation engine.
            - **Team C (Interview):** Builds a tool that analyzes video interview transcripts.
            **Fairness Challenge:** Bias can be introduced by any team and amplified by the next.
            """)

        with case_problem:
            st.markdown("""
            Each team operates in a silo, leading to systemic failure:
            1.  **Inconsistent Standards:** Team A and Team B use incompatible fairness metrics, negating each other's work.
            2.  **No Accountability Trail:** When Team C's model is found to be biased, there is no documentation explaining why risks were accepted.
            3.  **Ambiguous Ownership:** When a complaint is filed, it's unclear which team is responsible, leading to finger-pointing.
            
            **Result:** A fragmented, high-risk system where fairness efforts are undermined, and the organization cannot defend its practices.
            """)
        
        with case_solution:
            st.markdown("The organization implements the **Organizational Integration Toolkit**. Here's the impact:")
            
            st.success("##### 1. A Central Governance Body Sets the Standard")
            st.markdown("The newly formed **AI Review Board** creates a company-wide policy mandating **Equal Opportunity** as the primary fairness metric for all teams, ensuring consistency.")

            st.success("##### 2. Roles and Responsibilities are Clarified")
            st.markdown("Using the **RASCI Matrix**, each Product Owner is made **Accountable** for their component's fairness. A **Fairness Champion** is assigned to the platform to **Support** all three teams.")

            st.success("##### 3. A Documentation System Connects the Teams")
            st.markdown("Each team must complete a **Model Card**. Team B's card now explicitly references the fairness guarantees documented in Team A's card, creating a clear dependency chain.")
            
            st.success("##### 4. A Clear Escalation Path Resolves Conflict")
            st.markdown("Team C finds they cannot meet the Equal Opportunity threshold for non-native speakers. The **Fairness Champion** escalates the issue to the **AI Review Board**. The Board makes an informed, binding decision to invest in better training data rather than deploying a risky model.")
            
            st.info("**Result:** The governance framework transforms the siloed teams into a cohesive system. Standards are consistent, decisions are documented, and responsibilities are clear, significantly reducing the organization's risk.")

    st.markdown("---")

    # --- 7. Bibliography and Further Reading ---
    st.subheader("📚 Further Reading & Bibliography")
    with st.expander("Expand to see key resources for the Organizational Integration Toolkit"):
        st.markdown("""
        Effective organizational governance is the bridge between team-level fairness efforts and enterprise-wide accountability. The following resources provide the academic and practical foundations for the concepts in this toolkit.

        ##### Foundational Readings on AI Governance & Accountability:

        - **Raji, I. D., et al. (2020). *Closing the AI accountability gap: Defining an end-to-end framework for internal algorithmic auditing.***
          - **Why it's important:** This paper provides a comprehensive framework for accountability that inspires many of this toolkit's components, including governance gates, documentation standards, and escalation procedures. It is essential for understanding how to build a defensible fairness program.
        
        - **Metcalf, J., et al. (2021). *Algorithmic impact assessments and accountability: The co-construction of impacts.***
          - **Why it's important:** This work explores the practicalities of impact assessments, a key function of any AI governance body. It highlights the need for cross-functional collaboration, which underpins the RASCI matrix and the formation of an AI Review Board.

        - **Rakova, B., et al. (2021). *Where responsible AI meets reality: Practitioner perspectives on enablers for shifting organizational practices.***
          - **Why it's important:** Provides real-world insights into what's needed to shift organizational culture toward responsible AI, reinforcing the need for clear roles, leadership buy-in, and standardized processes.

        ##### On Specific Toolkit Components:

        - **For Roles & Responsibilities:** **Holstein, K., et al. (2019). *Improving fairness in machine learning systems: What do industry practitioners need?***
          - **Why it's important:** This research shows that practitioners need clear roles and responsibilities. It provides evidence for why hybrid organizational models (e.g., a central "Center of Excellence" with embedded "Fairness Champions") are often more effective than purely centralized or decentralized approaches.
        
        - **For Documentation:** **Mitchell, M., et al. (2019). *Model cards for model reporting.***
          - **Why it's important:** The foundational paper that introduced the concept of "Model Cards." This toolkit's documentation section is a direct application of this idea, extending it to include more explicit fairness and intersectional analysis.

        - **For Dashboards & Monitoring:** **Mehrabi, N., et al. (2021). *A survey on bias and fairness in machine learning.***
          - **Why it's important:** While a broad survey, it covers the necessity of post-deployment monitoring for fairness drift, which is the core concept behind the monitoring and alerting frameworks in this toolkit.
        """)

# --- PART 3: ADVANCED ARCHITECTURE COOKBOOK ---
with part3:
    st.header("Part 3: Advanced Architecture Cookbook 🍳")
    st.info(
        "**Objective:** To provide specialized, ready-to-use strategies that translate general fairness principles into concrete technical solutions for specific AI architectures. This cookbook addresses the reality that a 'one-size-fits-all' approach to fairness is insufficient for complex systems."
    )
    st.markdown("---")

    # --- 1. How to Use This Cookbook ---
    st.subheader("🚀 How to Use This Cookbook: A 5-Step Guide")
    st.markdown("Follow this process to select and implement the right fairness recipe for your project.")
    
    cols = st.columns(5)
    with cols[0]:
        st.markdown("##### 1. Identify Architecture")
        with st.popover("Details"):
            st.markdown("Select the tab below that matches your AI system's architecture (e.g., LLM, Recommender).")

    with cols[1]:
        st.markdown("##### 2. Understand Risks")
        with st.popover("Details"):
            st.markdown("Read the summary of common fairness challenges for that architecture to contextualize your work.")
    
    with cols[2]:
        st.markdown("##### 3. Select a Recipe")
        with st.popover("Details"):
            st.markdown("Choose a specific technical recipe that addresses a risk relevant to your project.")

    with cols[3]:
        st.markdown("##### 4. Integrate into Sprint")
        with st.popover("Details"):
            st.markdown("Use the provided guidance and code to create fairness tasks in your sprint backlog, as defined in the **Part 1: Fair AI Scrum Toolkit**.")

    with cols[4]:
        st.markdown("##### 5. Report Metrics")
        with st.popover("Details"):
            st.markdown("Ensure the metrics generated by the recipe are documented in your **Fairness Impact Statement** and reported to the governance body, as established in **Part 2**.")
    
    st.markdown("---")

    # --- 2. The Cookbook Recipes & Model Selection ---
    st.subheader("📚 The Cookbook: Recipes & Model Selection")
    
    card_tab, llm_tab, rec_tab, vision_tab, multi_tab = st.tabs([
        "**📜 Selecting Models with Model Cards**",
        "Large Language Models (LLMs)", 
        "Recommendation & Ranking Systems", 
        "Computer Vision Models", 
        "Multi-Modal Systems"
    ])

    # --- TAB: MODEL CARDS ---
    with card_tab:
        st.markdown("#### Selecting the Right Foundation: Using Model Cards")
        st.markdown("Before you apply any recipe, you must select the right ingredients. For AI, this often means choosing a pre-trained model. **Model Cards** are essential documents that describe a model's performance, intended use, and limitations, helping you make an informed and responsible choice (Mitchell et al., 2019).")

        st.info("💡 **Interactive Scenario: Choosing a Toxicity Classifier**")
        st.markdown("Your team needs a model to detect toxic comments for a social media platform with a diverse, global user base. Below are three potential models. Review their model cards and choose the most appropriate one.")

        with st.expander("**Model A: Toxicity Master 5000**"):
            st.markdown("""
            - **Intended Use:** General-purpose toxicity detection for formal English text.
            - **Performance:** 95% overall accuracy on benchmark datasets.
            - **Fairness Analysis:** Analysis performed on gender-related terms shows minimal bias.
            - **⚠️ Creator's Warnings & Limitations:** *Model was trained primarily on news articles and encyclopedia text. Performance on informal language or dialects like African American Vernacular English (AAVE) is not guaranteed and has been shown to have a higher false positive rate in internal tests.*
            """)

        with st.expander("**Model B: Dialect-Aware Classifier**"):
            st.markdown("""
            - **Intended Use:** Toxicity detection for user-generated content, including multiple English dialects.
            - **Performance:** 89% overall accuracy on benchmark datasets.
            - **Fairness Analysis:** Disaggregated performance shows consistent accuracy (<2% difference) across standard English, AAVE, and Indian English. The model was evaluated against the Jigsaw Unintended Bias dataset.
            - **⚠️ Creator's Warnings & Limitations:** *The model's larger size results in higher inference latency compared to smaller models. May not be suitable for real-time applications with very strict budgets.*
            """)
        
        with st.expander("**Model C: QuickTox v0.1**"):
            st.markdown("""
            - **Intended Use:** Fast text classification.
            - **Performance:** Accuracy is reported to be high.
            - **Fairness Analysis:** *No fairness analysis provided.*
            - **⚠️ Creator's Warnings & Limitations:** *Model is experimental. Use at your own risk.*
            """)
        
        st.divider()
        
        selection = st.radio(
            "**Which model is the most appropriate for your use case?**",
            ("Model A: Toxicity Master 5000", "Model B: Dialect-Aware Classifier", "Model C: QuickTox v0.1"),
            index=None,
            key="model_card_choice"
        )

        if selection == "Model B: Dialect-Aware Classifier":
            st.success("""
            **Correct Choice.** Although its overall accuracy is lower, Model B is the most responsible choice. Its model card explicitly states that it was tested for fairness across different dialects, directly addressing a key risk for a social media platform. The known limitation (latency) is a manageable engineering trade-off.
            """)
        elif selection == "Model A: Toxicity Master 5000":
            st.warning("""
            **Risky Choice.** While its accuracy is high, the model card contains a critical warning: it performs poorly on the exact type of informal language and dialects your platform will have. Deploying this model would likely lead to unfair censorship of minority groups.
            """)
        elif selection == "Model C: QuickTox v0.1":
            st.error("""
            **Very Risky Choice.** The lack of a proper model card, especially the absence of any fairness analysis or clear limitations, is a major red flag. Using this model would be irresponsible as you have no information about its potential to cause harm.
            """)

        st.subheader("Checklist: How to Read a Model Card for Fairness")
        st.markdown("""
        - **[ ] Match Use Case:** Does the model's *intended use* align with your specific application? A mismatch is a primary source of risk.
        - **[ ] Check the Data:** On what datasets was the model trained and, more importantly, *evaluated*? Do these datasets reflect your user population?
        - **[ ] Scrutinize Fairness Metrics:** What fairness metrics are reported? Are they relevant to the harms you want to prevent (e.g., Equal Opportunity for a screening tool)?
        - **[ ] Heed the Warnings:** Pay closest attention to the **Limitations and Warnings** section. The creators are telling you where the model is likely to fail.
        - **[ ] Look for Gaps:** What's *not* on the card? The absence of fairness testing or disaggregated performance analysis is as telling as the presence of a bad result.
        """)

    with llm_tab:
        st.markdown("#### Fairness in Large Language Models (LLMs)")
        st.markdown("LLMs present unique bias patterns through their training data and generative processes. A generic approach is ineffective for these models.")

        with st.expander("Key Challenges & Concepts for LLMs"):
            st.error("##### Pre-training Data Bias and Amplification")
            st.markdown("LLMs are pre-trained on massive web corpora containing historical biases, stereotypes, and harmful content. These biases don't just transfer—they can be amplified. This connects to Bender et al.'s (2021) work illustrating how models trained on internet corpora inherit and amplify societal biases.")
            st.info("##### Emergent Behaviors and Safety Guardrails")
            st.markdown("LLMs exhibit **emergent capabilities** that appear only at scale (e.g., in-context learning, sycophancy), creating fairness challenges that require specialized guardrails, as simple metrics are insufficient.")
            st.warning("##### Frequent Mistakes")
            st.markdown("A common mistake is assuming a model fine-tuned on a balanced dataset is free from bias; biases from the original pre-training can persist and re-emerge in unexpected ways.")

        st.subheader("LLM Fairness Recipes")
        st.markdown("Select a recipe to see its implementation details.")
        
        with st.expander("Recipe 1: Fairness Prompting & Self-Critique"):
            st.markdown("""
            - **Objective:** To guide the model toward fairer, less stereotypical outputs at inference time without retraining.
            - **When to Apply:** Ideal when you have API access to a model but cannot fine-tune it. This is a crucial **Post-processing** technique.
            - **Key Metric:** Reduction in stereotypical associations; increased consistency in responses across counterfactual prompts.
            - **Integration:** The prompt design and its effectiveness should be documented in the **Fairness Impact Statement (Part 2)**.
            """)
            
            st.markdown("##### 💡 Interactive Simulation: Self-Critique Prompting")
            st.markdown("The model generates an initial, potentially biased summary. The self-critique prompt then forces it to revise.")

            initial_summary = "A very nurturing and collaborative female engineer who is a great team player."
            critique_prompt = "Critique the previous summary for potential gender stereotypes and rewrite it to be neutral and skill-focused."
            revised_summary = "An engineer with 5 years of experience in Python and cloud architecture, who has successfully led three major projects to completion."

            st.error(f"**Initial Model Output:** *{initial_summary}*")
            if st.checkbox("Apply Self-Critique Prompt"):
                st.code(f"PROMPT: {critique_prompt}", language="markdown")
                st.success(f"**Revised Model Output:** *{revised_summary}*")
                st.caption("The revised output successfully removes subjective, potentially stereotypical language and focuses on verifiable achievements.")

            with st.popover("How to Apply: Step-by-Step"):
                st.markdown("""
                1.  **Design a Fairness Prompt:** Add explicit instructions to your system prompt. For example: *"You are an AI assistant. Ensure your responses are impartial and do not rely on stereotypes related to gender, race, or age."*
                2.  **Create a Self-Critique Framework:** For high-stakes generation, use a two-step process. First, generate a response. Second, use another prompt to ask the LLM to check its own work: *"Review the following text for hidden biases. If any are found, rewrite it."*
                3.  **Implement Counterfactual Testing:** To validate, create prompts that are identical except for a demographic attribute (e.g., "Describe a successful male doctor" vs. "Describe a successful female doctor") and measure the difference in the generated descriptions.
                """)
        
        with st.expander("Recipe 2: Fairness-Aware Fine-Tuning"):
            st.markdown("""
            - **Objective:** To specialize a pre-trained LLM for a specific task while actively reducing inherited biases.
            - **When to Apply:** When you have the resources to fine-tune a model and need to align it with specific domain and fairness requirements. This is an **In-processing** technique.
            - **Key Metric:** Improvement on fairness benchmark suites (e.g., reduced toxicity, stereotype scores) while maintaining performance on the primary task.
            - **Integration:** The fine-tuning dataset and methodology must be documented in the **Compliance Addendum (Part 4)** under Data Governance.
            """)
            st.markdown("##### How to Apply: Step-by-Step")
            st.markdown("""
                1.  **Curate a Balanced Fine-tuning Dataset:** Create or gather a dataset that has diverse, representative examples. For instance, if fine-tuning for a customer service bot, ensure the examples include interactions with people from various linguistic backgrounds.
                2.  **Use Counterfactual Data Augmentation:** For each training example, create an alternate version where demographic attributes are swapped. For example: "The doctor advised his patient" becomes "The doctor advised her patient." Training on both helps the model de-correlate gender from professions.
                3.  **Implement Fairness-Specific RLHF:** In Reinforcement Learning from Human Feedback, instruct human labelers to explicitly rank responses not just on helpfulness, but also on fairness. A response that is helpful but contains a microaggression should be ranked lower than one that is slightly less helpful but fair.
                """)
                
        with st.expander("🌍 Intersectional Considerations for LLMs"):
            st.markdown("""
            Traditional LLM fairness often addresses single dimensions of bias (e.g., gender stereotypes). This misses critical intersectional patterns. As Crenshaw (1989) noted, the experience of a Black woman is not simply the sum of racism and sexism.
            - **Action:** Design prompt templates and fine-tuning datasets that explicitly reference and test intersectional identities (e.g., "Describe a successful older, female, immigrant scientist").
            - **Evaluation:** Use red-teaming and evaluation frameworks to specifically probe for biases against intersectional groups, as these are often where the most harmful stereotypes emerge.
            """)

    with rec_tab:
        st.markdown("#### Fairness in Recommendation & Ranking Systems")
        st.markdown("These systems can create feedback loops that amplify biases and lead to unfair exposure for certain items or creators.")

        with st.expander("Key Challenges & Concepts for Recommendation Systems"):
            st.error("##### Multi-Stakeholder Fairness Tensions")
            st.markdown("Systems must balance the needs of **users** (who want relevance), **item providers** (who want fair exposure), and the **platform** (which has business goals). These needs often conflict.")
            st.info("##### Feedback Loops & Preference Amplification")
            st.markdown("A key challenge is that the model's own recommendations shape the data it learns from. An initial small bias can become extreme over time as popular items get recommended more, receive more clicks, and thus appear even more popular to the algorithm.")
            st.warning("##### Diversity-Relevance Trade-offs")
            st.markdown("A model optimized purely for relevance may create 'filter bubbles,' showing users only what they already like and limiting discovery. Fairness often requires intentionally injecting diversity, which may slightly reduce short-term relevance metrics.")

        st.subheader("Recommendation Fairness Recipes")
        with st.expander("Recipe 1: Re-ranking for Provider Diversity"):
            st.markdown("""
            - **Objective:** To mitigate exposure disparity by adjusting the final ranked list of recommendations to ensure items from different provider groups are fairly represented.
            - **When to Apply:** As a **Post-processing** step after the initial relevance scores have been generated by the main recommendation model.
            - **Key Metric:** Exposure parity (the proportion of a group in top-K recommendations should be similar to their proportion in the catalog).
            - **Integration:** The chosen level of exposure parity is a strategic decision that must be approved by the **AI Review Board (Part 2)**, as it involves a direct trade-off.
            """)
            
            st.markdown("##### 💡 Interactive Simulation: Re-ranking for Exposure")
            
            st.code("""
# Conceptual Re-ranking Algorithm
def fair_rerank(items_with_scores, fairness_boost):
    for item in items_with_scores:
        if item.is_underrepresented:
            item.final_score = item.relevance_score + fairness_boost
        else:
            item.final_score = item.relevance_score
    return sorted(items_with_scores, key=lambda x: x.final_score, reverse=True)
            """, language="python")

            fairness_boost = st.slider("Fairness Boost for Minority Group Items", 0.0, 1.0, 0.2, 0.05, key="p3_slider")
            
            catalog_prop_a, catalog_prop_b = 0.7, 0.3
            rec_prop_a_base, rec_prop_b_base = 0.9, 0.1
            
            boost_effect = rec_prop_a_base * fairness_boost
            rec_prop_a_final = rec_prop_a_base - boost_effect
            rec_prop_b_final = rec_prop_b_base + boost_effect
            
            plot_df = pd.DataFrame({
                'Group': ['Majority Provider', 'Minority Provider', 'Majority Provider', 'Minority Provider'],
                'Source': ['Item Catalog', 'Item Catalog', 'Top Recommendations', 'Top Recommendations'],
                'Proportion': [catalog_prop_a, catalog_prop_b, rec_prop_a_final, rec_prop_b_final]
            })

            chart = alt.Chart(plot_df).mark_bar().encode(
                x=alt.X('Proportion', type='quantitative', axis=alt.Axis(format='%')),
                y='Source:N',
                color='Group:N',
                tooltip=['Group', 'Proportion']
            ).properties(title="Representation in Catalog vs. Recommendations")
            
            st.altair_chart(chart, use_container_width=True)
            st.caption("By applying a 'fairness boost,' the re-ranking algorithm increases the final score of items from the minority provider group, moving them higher in the list and improving their exposure in the top recommendations.")

            with st.popover("How to Apply: Step-by-Step"):
                st.markdown("""
                1. **Define Provider Groups:** Tag items in your catalog with relevant provider attributes (e.g., 'new_creator', 'minority_owned_business').
                2. **Calculate Baseline Exposure:** Run your standard recommendation model and measure the representation of each provider group in the top-K results. Compare this to their representation in the overall catalog.
                3. **Implement a Re-ranking Function:** Create a post-processing function that takes the initial list of ranked items. The function should iterate through the list and apply a score adjustment (a 'boost') to items from underrepresented groups.
                4. **Tune the Boost Parameter:** The size of the boost is a hyperparameter that controls the trade-off between relevance and fairness. Tune this parameter on a validation set to find a point that meets your fairness goals without excessively harming relevance.
                """)
        
        with st.expander("🌍 Intersectional Considerations for Recommendation Systems"):
            st.markdown("""
            As shown by Noble's (2018) work on search algorithms, systems can perpetuate harmful stereotypes against intersectional groups (e.g., Black women).
            - **Action:** Define provider groups intersectionally (e.g., 'female creators, non-US'). Your re-ranking and monitoring must track exposure for these specific subgroups.
            - **Evaluation:** When analyzing user-side fairness, check if recommendation quality is consistent across intersectional user groups. The system may be highly relevant for men and for white users, but fail for white women or men of color.
            """)

    with vision_tab:
        st.markdown("#### Fairness in Computer Vision Models")
        st.markdown("Vision models can exhibit significant performance disparities, often failing on demographic intersections (e.g., women with darker skin) that aggregate metrics hide.")

        with st.expander("Key Challenges & Concepts for Computer Vision"):
            st.error("##### Visual Representation Bias")
            st.markdown("CNN layers can learn to extract features correlated with race, gender, and age even when it is not the intended task. The model might learn to associate certain backgrounds or lighting conditions with specific demographics.")
            st.info("##### Data Collection and Capture Conditions")
            st.markdown("Bias can be introduced before the model is even trained. The **image capture pipeline** itself (camera sensors, lighting) can perform differently for different skin tones. Datasets are often not representative of global populations.")
            st.warning("##### Frequent Mistakes")
            st.markdown("Reporting only **overall accuracy** is highly misleading. A model can be 95% accurate overall but have a 30% error rate for a specific intersectional group, a critical failure described by Buolamwini & Gebru (2018).")
            
        st.subheader("Computer Vision Fairness Recipes")
        with st.expander("Recipe 1: Disaggregated Performance Analysis"):
            st.markdown("""
            - **Objective:** To move beyond aggregate accuracy and evaluate model performance across distinct demographic subgroups.
            - **When to Apply:** This should be a **mandatory** validation step for any vision model that analyzes human features.
            - **Key Metric:** Any standard classification metric (Accuracy, Error Rate) disaggregated by subgroup.
            - **Integration:** This is a required validation for the **Definition of Done (Part 1)** and must be reported to the **AI Review Board (Part 2)**.
            """)

            st.markdown("##### 💡 Interactive Example: Detecting Performance Gaps with `Fairlearn`")
            st.markdown("This example uses `Fairlearn`'s `MetricFrame` to easily slice performance metrics across sensitive features.")
            
            data = {
                'true_label': [1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0],
                'prediction': [1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
                'skin_tone': ['Light', 'Light', 'Light', 'Light', 'Dark', 'Dark', 'Dark', 'Dark', 'Dark', 'Dark', 'Light', 'Dark'],
            }
            df_vision = pd.DataFrame(data)

            metrics = {'accuracy': accuracy_score}
            grouped_on_skin_tone = MetricFrame(metrics=metrics,
                                                y_true=df_vision['true_label'],
                                                y_pred=df_vision['prediction'],
                                                sensitive_features=df_vision['skin_tone'])

            st.metric(label="Overall Accuracy", value=f"{grouped_on_skin_tone.overall['accuracy']:.2%}")
            st.markdown("##### Accuracy by Perceived Skin Tone")
            st.dataframe(grouped_on_skin_tone.by_group, use_container_width=True)

            accuracy_by_group = grouped_on_skin_tone.by_group
            # Ensure we handle the Series correctly
            if isinstance(accuracy_by_group, pd.Series):
                accuracy_gap = accuracy_by_group.diff().iloc[-1]
            else: # It's a DataFrame
                accuracy_gap = accuracy_by_group['accuracy'].diff().iloc[-1]
            
            st.error(f"The results clearly show a performance gap: the model's accuracy is **{abs(accuracy_gap):.2%}** lower for the 'Dark' skin tone group. This is a critical fairness issue.")

            with st.popover("How to Apply: Step-by-Step"):
                st.markdown("""
                1. **Acquire Labeled Data:** Obtain a validation dataset with reliable labels for the demographic attributes you need to test (e.g., skin tone, gender).
                2. **Choose Your Metrics:** Decide which performance metrics are most important for your use case (e.g., accuracy, false negative rate).
                3. **Use `MetricFrame`:** The `fairlearn` library is the industry standard for this. Create a `MetricFrame` object, passing in your metrics, true labels, predictions, and the sensitive features you want to group by.
                4. **Analyze Results:** Examine both the `.overall` metric and the `.by_group` metrics. Calculate the `.difference()` or `.ratio()` to quantify the disparity. Any large gap indicates a fairness problem that must be addressed.
                """)
        
        with st.expander("🌍 Intersectional Considerations for Computer Vision"):
            st.markdown("""
            As the 'Gender Shades' project famously demonstrated, intersectional failures are the most common and severe in computer vision. A model might work well for men and for light-skinned individuals, but fail catastrophically for dark-skinned women.
            - **Action:** Your disaggregated analysis **must** be intersectional. Create a combined feature (e.g., `gender_skin_tone`) and use that as the sensitive attribute in your `MetricFrame` analysis.
            - **Data Collection:** When augmenting or collecting new data, prioritize filling gaps for the worst-performing intersectional subgroups.
            """)

    with multi_tab:
        st.markdown("#### Fairness in Multi-Modal Systems")
        st.markdown("Multi-modal systems combine challenges from different architectures. Bias can emerge from a single modality or from flawed interactions between them.")
        
        with st.expander("Key Challenges & Concepts for Multi-Modal Systems"):
            st.error("##### Cross-Modal Bias Amplification")
            st.markdown("Bias from one modality (e.g., a speech-to-text model that performs poorly on accented speech) can 'poison' the entire system, leading to an incorrect final decision even if other modalities (like video) are neutral.")
            st.info("##### Modality Dominance")
            st.markdown("The model may learn to over-rely on one modality for certain groups. For example, it might rely on visual cues for one demographic group but on audio cues for another, leading to inconsistent and unfair evaluations.")
            st.warning("##### Fusion Layer Bias")
            st.markdown("The **shared latent space** where modalities are fused can propagate or amplify hidden biases in ways that are very hard to detect. The fusion process itself can create new biases not present in any single modality.")

        st.subheader("Multi-Modal Fairness Recipes")
        with st.expander("Recipe 1: Cross-Modal Consistency Check"):
            st.markdown("""
            - **Objective:** To check if the model's prediction remains stable when one modality is removed or altered. Inconsistency can reveal over-reliance on a biased modality.
            - **When to Apply:** During model evaluation and debugging, especially when you suspect modality dominance.
            - **Key Metric:** Prediction Agreement Rate (how often the prediction is the same with and without a modality).
            - **Integration:** This is an advanced testing strategy that can be added as an acceptance criterion to a **User Story (Part 1)** for high-risk systems.
            """)
            
            st.markdown("##### 💡 Interactive Simulation: Modality Dominance")
            st.markdown("Imagine an AI system analyzing a video interview for a 'confidence' score. See how the final score can be swayed by just one modality.")

            text_score = st.slider("Score from Transcript (Text)", 0.0, 1.0, 0.8, key="mm_text")
            video_score = st.slider("Score from Body Language (Vision)", 0.0, 1.0, 0.7, key="mm_video")
            audio_score = st.slider("Score from Vocal Tone (Audio)", 0.0, 1.0, 0.3, key="mm_audio")
            
            modality_weights = {"Text": 0.33, "Vision": 0.33, "Audio": 0.34}
            dominant_modality = st.radio("Simulate a biased model that over-weights one modality:", list(modality_weights.keys()), horizontal=True, key="mm_dom")

            if dominant_modality == "Audio":
                modality_weights = {"Text": 0.1, "Vision": 0.1, "Audio": 0.8}
            elif dominant_modality == "Vision":
                modality_weights = {"Text": 0.1, "Vision": 0.8, "Audio": 0.1}
            else: # Text
                modality_weights = {"Text": 0.8, "Vision": 0.1, "Audio": 0.1}

            final_score = (text_score * modality_weights["Text"]) + (video_score * modality_weights["Vision"]) + (audio_score * modality_weights["Audio"])

            st.metric(label="Final Confidence Score", value=f"{final_score:.2%}")

            if final_score < 0.5:
                st.warning(f"Notice how the low **{dominant_modality}** score is disproportionately pulling down the final assessment. This is **Modality Dominance**, a key fairness risk if that modality is less accurate for certain demographic groups.")
            else:
                st.success("The scores are more balanced. A fair fusion mechanism should prevent one modality from unfairly dominating the outcome.")

            with st.popover("How to Apply: Step-by-Step"):
                st.markdown("""
                1.  **Get a Baseline Prediction:** Run your multi-modal model on a validation sample and store the prediction.
                2.  **Perform Modality Ablation:** Run the model again on the same sample, but this time "zero out" or remove one of the modalities (e.g., replace the image with a blank tensor, or the audio with silence).
                3.  **Compare Predictions:** Check if the prediction changed. Do this for each modality.
                4.  **Disaggregate Results:** Perform this analysis separately for different demographic groups. If you find that removing the audio modality changes the prediction for Group A 80% of the time, but only 20% of the time for Group B, it indicates the model is relying on audio unfairly for Group A.
                """)

        with st.expander("🌍 Intersectional Considerations for Multi-Modal Systems"):
            st.markdown("""
            Intersectional bias in multi-modal systems can be particularly insidious. For example, a speech recognition system (audio modality) might perform poorly for women with non-native accents, and a gesture recognition system (vision modality) might misinterpret cultural gestures. For a woman with a non-native accent using culturally specific gestures, the system could fail on both modalities, leading to a compounded, severe bias.
            - **Action:** Your cross-modal consistency checks must be performed on intersectional subgroups.
            - **Evaluation:** When evaluating, specifically look for cases where the model fails on *multiple* modalities for the same intersectional group.
            """)

    st.markdown("---")

    # --- 7. Bibliography and Further Reading ---
    st.subheader("📚 Further Reading & Bibliography")
    with st.expander("Expand to see key resources for the Advanced Architecture Cookbook"):
        st.markdown("""
        The strategies in this cookbook are derived from leading research into the fairness challenges unique to complex AI architectures. These references provide deeper technical and conceptual background for the recipes provided.

        ##### Foundational Readings on Architectural Fairness:

        - **Bommasani, R., et al. (2021). *On the opportunities and risks of foundation models.***
          - **Why it's important:** This comprehensive paper outlines the unique societal risks, including fairness, posed by large-scale, pre-trained "foundation models" like LLMs. It provides the context for why these models need specialized fairness approaches.
        
        - **Bender, E. M., et al. (2021). *On the dangers of stochastic parrots: Can language models be too big?***
          - **Why it's important:** A critical examination of the harms embedded in the massive web-scale datasets used to train LLMs. It explains the source of many of the biases that the LLM recipes in this cookbook are designed to mitigate.
        
        - **Buolamwini, J., & Gebru, T. (2018). *Gender shades: Intersectional accuracy disparities in commercial gender classification.***
          - **Why it's important:** The landmark study that revealed severe intersectional bias in commercial computer vision systems. It is the foundational text for understanding why disaggregated and intersectional evaluation is non-negotiable for vision models.

        ##### On Specific Architectures:

        - **For LLMs:** **Liang, P. P., et al. (2022). *Holistic evaluation of language models.***
          - **Why it's important:** Proposes a multi-faceted approach to evaluating LLMs that goes beyond simple accuracy to include fairness, robustness, and other dimensions. This informs the evaluation strategies for the LLM recipes.
        
        - **For Recommendation Systems:** **Burke, R. (2017). *Multisided fairness for recommendation.***
          - **Why it's important:** This paper is essential for understanding the core challenge in recommender fairness: balancing the needs of multiple stakeholders (users, item providers, the platform). It frames the problem that many of the cookbook's re-ranking and diversity recipes aim to solve.
        
        - **For Vision & Multi-Modal Systems:** **Wang, Z., et al. (2022). *Towards fairness in visual recognition: Effective strategies for bias mitigation.***
          - **Why it's important:** Provides a practical overview of different bias mitigation strategies for computer vision, aligning with the cookbook's recipe-based format. It covers data-centric, in-processing, and post-processing approaches.
        """)

#PART 4:
with part4:
    st.header("Part 4: Regulatory Compliance & Risk Alignment ⚖️")
    st.info(
        "**Objective:** To translate abstract legal obligations from regulations like the EU AI Act and GDPR into concrete development tasks, governance controls, and documentation. This guide ensures that your fairness implementation is not just ethical and technical, but also legally defensible."
    )
    st.markdown("---")

    # --- Main Tabs for Part 4 ---
    (
        tab_guide,
        tab_risk,
        tab_translation,
        tab_eu,
        tab_evidence,
        tab_case_study,
    ) = st.tabs([
        "**🚀 How to Use This Guide**",
        "**🌍 Global Landscape & Risk Classification**",
        "**⚖️ Translating Law to Code**",
        "**🇪🇺 EU AI Act & GDPR Deep Dive**",
        "**📄 Evidence Collection & Audit Trails**",
        "**🎓 Case Study: University Admissions**"
    ])

    # --- TAB 1: HOW TO USE THIS GUIDE ---
    with tab_guide:
        st.subheader("How to Use This Guide: A 5-Step Process")
        st.markdown("Follow this process to align your AI development lifecycle with regulatory requirements.")
        
        cols = st.columns(5)
        with cols[0]:
            st.markdown("##### 1. Classify System Risk")
            with st.popover("Details"):
                st.markdown("Use the **Risk Classification Calculator** in the next tab to determine the risk level of your AI system (e.g., Low, High). This is the most critical first step.")
        
        with cols[1]:
            st.markdown("##### 2. Identify Controls")
            with st.popover("Details"):
                st.markdown("The risk level will automatically trigger a set of required compliance controls, such as mandatory documentation, human oversight, or data governance checks.")
        
        with cols[2]:
            st.markdown("##### 3. Map to Sprint Tasks")
            with st.popover("Details"):
                st.markdown("Use the **Regulatory Mapping Framework** to translate the required controls into specific user stories, backlog tasks, and Definition of Done criteria for your team.")
        
        with cols[3]:
            st.markdown("##### 4. Implement Governance Gates")
            with st.popover("Details"):
                st.markdown("Ensure that your project cannot proceed to deployment without satisfying the controls for its risk level. This is enforced by the **AI Review Board (Part 2)**.")
        
        with cols[4]:
            st.markdown("##### 5. Maintain Audit Trail")
            with st.popover("Details"):
                st.markdown("Use the **Evidence Collection** templates and frameworks to continuously capture the evidence needed to demonstrate compliance to auditors or regulators.")

    # --- TAB 2: GLOBAL LANDSCAPE & RISK CLASSIFICATION ---
    with tab_risk:
        st.subheader("Global Regulatory Landscape")
        with st.expander("Common Principles Across Global Frameworks"):
            st.markdown("""
            Despite regional differences, most AI regulations are converging on a set of core principles. Understanding these helps create a unified compliance strategy.
            - **Risk-Based Regulation:** Stricter rules for higher-risk systems.
            - **Fairness Impact Assessment:** A mandatory evaluation of fairness implications before deployment.
            - **Human Oversight:** Mechanisms for human review of significant automated decisions.
            - **Documentation & Record-Keeping:** Maintaining detailed records for accountability.
            - **Transparency Obligations:** Providing clear information about how AI systems function.
            """)

        st.subheader("Multi-Factor Risk Classification Calculator")
        st.markdown("Effective risk assessment is multi-dimensional. Rate your system on the following factors to determine its **inherent risk level** (the risk before mitigation controls are applied).")
        
        # Interactive Multi-Factor Calculator
        domain_impact_map = {"Low": 1, "Medium": 3, "High": 5}
        autonomy_map = {"Human in the loop": 1, "Human over the loop": 3, "Fully Autonomous": 5}
        decision_impact_map = {"Informational": 1, "Affects Opportunities": 3, "Life-Altering": 5}
        scale_map = {"< 1k people": 1, "1k - 100k people": 3, "> 100k people": 5}

        q1 = st.select_slider("**1. Domain Impact:** What is the typical impact of decisions in this domain?", options=domain_impact_map.keys(), value="Medium", key="p4_q1")
        q2 = st.select_slider("**2. Autonomy Level:** How much human oversight is involved in a typical decision?", options=autonomy_map.keys(), value="Human over the loop", key="p4_q2")
        q3 = st.select_slider("**3. Decision Impact:** How significant is the system's impact on an individual's rights or opportunities?", options=decision_impact_map.keys(), value="Affects Opportunities", key="p4_q3")
        q4 = st.select_slider("**4. Scale:** How many people will be affected by the system in a year?", options=scale_map.keys(), value="1k - 100k people", key="p4_q4")
        
        total_score = domain_impact_map[q1] + autonomy_map[q2] + decision_impact_map[q3] + scale_map[q4]

        risk_level = "Minimal / Low Risk"
        if 8 <= total_score <= 12:
            risk_level = "Limited Risk"
        elif total_score > 12:
            risk_level = "High Risk"
            
        st.divider()
        st.metric(label="Calculated Risk Score", value=f"{total_score} / 20")
        st.markdown(f"#### Recommended Inherent Risk Classification: **{risk_level}**")
        st.caption("This classification determines which regulatory controls and governance procedures apply to your project.")
        st.divider()

        with st.expander("🌍 Intersectional Considerations for Risk Classification"):
            st.markdown("""
            Traditional risk assessment often misses how risks can be amplified for intersectional groups. A system might be medium-risk for the general population but high-risk for a specific subgroup (e.g., non-native speakers in a voice analysis system).
            - **Action:** During assessment, explicitly ask: *"Could the impact of this system be disproportionately severe for any intersectional group?"* If the answer is yes, consider increasing the 'Decision Impact' score.
            """)

    # --- TAB 3: TRANSLATING LAW TO CODE ---
    with tab_translation:
        st.subheader("Regulatory Mapping Framework: From Law to Code")
        st.markdown("This framework translates high-level legal requirements into actionable tasks for agile teams, connecting compliance directly to the development lifecycle.")

        with st.expander("**Requirement: Data Quality & Governance** (EU AI Act, Article 10)"):
            st.markdown("""
            - **📜 What it means:** The data used to train your model must be relevant, representative, and free of errors and biases.
            - **💻 Corresponding Sprint Task:**
              - Create a task to generate a "Datasheet for Datasets" to document data provenance, collection, and limitations.
              - Add a task for a bias audit on the training data.
            - **✅ Impact on Definition of Done (DoD):**
              - Add a criterion: *"Data bias audit has been completed and documented."*
            """)
            
        with st.expander("**Requirement: Human Oversight** (EU AI Act, Article 14)"):
            st.markdown("""
            - **📜 What it means:** High-risk systems must be designed so that a human can intervene or oversee their decisions.
            - **💻 Corresponding Sprint Task:**
              - Create a user story for a human-in-the-loop feature (e.g., "As an admin, I want to review and override the AI's high-impact decisions").
              - Design and test the UI/UX for this oversight mechanism.
            - **✅ Impact on Acceptance Criteria:**
              - The human override feature must be fully functional and tested.
            """)
            
        with st.expander("**Requirement: Transparency & Explainability** (GDPR, Article 22)"):
            st.markdown("""
            - **📜 What it means:** You must be able to provide meaningful information about the logic involved in automated decisions.
            - **💻 Corresponding Sprint Task:**
              - Implement a library like SHAP or LIME to generate local explanations for individual predictions.
              - Create an API endpoint to serve these explanations upon request.
            - **✅ Impact on Documentation (Audit Trail):**
              - The chosen explainability method and its limitations must be documented in the **Compliance Addendum**.
            """)

    # --- TAB 4: EU AI ACT & GDPR DEEP DIVE ---
    with tab_eu:
        st.subheader("Deep Dive into EU Regulations")
        eu_act_tab, gdpr_tab = st.tabs(["EU AI Act", "GDPR Article 22"])

        with eu_act_tab:
            st.markdown("#### The EU AI Act's Risk-Based Approach")
            with st.expander("The Four Risk Tiers"):
                st.markdown("""
                - **Unacceptable Risk:** Prohibited practices like social scoring or manipulation.
                - **High-Risk:** Systems in sensitive domains (e.g., hiring, credit) requiring robust compliance.
                - **Limited Risk:** Systems requiring transparency (e.g., chatbots must disclose they are AI).
                - **Minimal Risk:** Most AI systems, with no new legal obligations.
                """)
            with st.expander("Core Requirements for High-Risk Systems"):
                st.markdown("""
                1.  **Risk Management System:** A continuous process to identify and mitigate risks.
                2.  **Data Governance:** High standards for data quality, relevance, and bias examination.
                3.  **Technical Documentation:** Detailed records of design, development, and performance.
                4.  **Record-Keeping (Logging):** Automatic logging for traceability.
                5.  **Transparency & User Information:** Clear instructions and information for users.
                6.  **Human Oversight:** Mechanisms for meaningful human review and intervention.
                7.  **Accuracy, Robustness, and Cybersecurity:** High technical standards.
                """)

        with gdpr_tab:
            st.markdown("#### GDPR Article 22: Rights in Automated Decision-Making")
            st.markdown("This article grants individuals specific rights when they are subject to a purely automated decision with legal or similarly significant effects.")
            with st.expander("Key Rights and Principles"):
                st.markdown("""
                - **Right to Object:** Individuals can generally opt out of purely automated decisions.
                - **Right to an Explanation:** They must receive meaningful information about the logic involved.
                - **Right to Contest:** They can challenge the decision and request a human review.
                - **Safeguard Requirements:** Organizations must implement measures to prevent discriminatory outcomes.
                """)

        with st.expander("💡 FAQ: How do we comply with both the AI Act and GDPR?"):
            st.markdown("""
            Implement a **unified compliance approach**. Both frameworks have overlapping requirements for impact assessments, documentation, human oversight, and transparency.
            1.  Create a single, comprehensive technical documentation package that satisfies both.
            2.  Design a human oversight mechanism that fulfills the requirements of both regulations.
            3.  Then, address the unique elements of each (like GDPR's lawful basis) as extensions to your unified foundation.
            This layered approach, as suggested by researchers, can reduce compliance overhead significantly.
            """)

    # --- TAB 5: EVIDENCE COLLECTION & AUDIT TRAILS ---
    with tab_evidence:
        st.subheader("Evidence Collection & Creating a Defensible Audit Trail")
        st.markdown("Without systematic evidence, you can't demonstrate compliance. This section provides frameworks for creating audit trails that document fairness decisions and link evidence to specific requirements.")

        with st.expander("Key Concepts for Evidence Collection"):
            st.markdown("""
            - **Evidence Lifecycle Management:** Systematically plan, generate, validate, and store evidence throughout the AI lifecycle, rather than creating it last-minute.
            - **Requirement-Driven Documentation:** Map every documentation artifact directly to a specific regulatory requirement to ensure complete coverage without unnecessary work.
            - **Automated Evidence Generation:** Integrate evidence collection into your CI/CD pipeline. For example, automatically save fairness test reports from each build as a compliance artifact.
            """)
        
        st.subheader("Compliance Documentation Template (Addendum)")
        st.markdown("This template extends the **Fairness Impact Statement (Part 2)** to include fields specifically required for regulatory compliance.")

        compliance_addendum_template = """
# Compliance Addendum for [Name of AI System]
**Date:** 2025-09-22
**Version:** 1.1

### 1. Applicable Regulations & Legal Basis
*List the regulations this system is subject to (e.g., EU AI Act, GDPR Art. 22) and the legal basis for its data processing.*

### 2. Risk Classification
*State the result from the Risk Classification Calculator (e.g., High Risk) and a brief justification.*

### 3. Data Governance Log
*Link to "Datasheet for Datasets". Summarize steps taken to ensure data quality and mitigate bias, including dates and personnel involved.*

### 4. Human Oversight Mechanism
*Describe the implemented human oversight system. Detail the conditions under which a human is alerted, the information they are provided, and the scope of their authority to intervene.*

### 5. Log of Audits and Reviews
*Maintain a running log of all fairness and compliance reviews. Include dates, findings, and resolutions.*
        """
        st.code(compliance_addendum_template, language="markdown")
        st.download_button(
            label="Download Compliance Addendum Template (.md)",
            data=compliance_addendum_template,
            file_name="Compliance_Addendum_Template.md",
            mime="text/markdown"
        )
        
        with st.expander("🌍 Intersectional Considerations for Evidence Collection"):
            st.markdown("""
            Regulatory frameworks often address protected attributes independently. Your evidence collection must go further.
            - **Action:** Your documentation must show explicit consideration of intersectional impacts. For example, the "Data Governance Log" should describe how you audited for representation gaps in intersectional subgroups, not just individual groups.
            - **Testing Evidence:** Your stored test results must include performance data disaggregated by intersectional groups.
            """)

    # --- TAB 6: CASE STUDY: UNIVERSITY ADMISSIONS ---
    with tab_case_study:
        st.subheader("Case Study: AI-Powered University Admissions System")
        st.markdown("A university implements an AI tool to help review student applications. Here's how they use the compliance guide.")
        
        cs_context, cs_problem, cs_solution = st.tabs(["Context", "The Problem (Without This Guide)", "The Solution (With This Guide)"])
        
        with cs_context:
            st.markdown("""
            - **System:** An AI model that provides a "readiness score" for university applicants based on grades, essays, and extracurriculars.
            - **Goal:** To help admissions officers handle a large volume of applications more efficiently.
            - **Jurisdiction:** Operates within the European Union.
            """)
        
        with cs_problem:
            st.markdown("""
            The development team, under pressure to deliver, makes several compliance errors:
            1.  **Misclassification:** They classify the system as "Limited Risk" because it only provides a score, not a final decision. They fail to recognize its significant impact on educational opportunities.
            2.  **Disconnected Compliance:** The legal team provides a summary of GDPR, but the developers don't know how to translate it into specific tasks. They ignore it.
            3.  **No Audit Trail:** When an external audit asks how they ensure fairness, the team has no documentation of their data quality checks or bias testing, even though they performed some.
            
            **Result:** The university deploys a high-risk system without the required safeguards, exposing them to significant legal fines and reputational damage.
            """)
        
        with cs_solution:
            st.markdown("The team adopts the **Regulatory Compliance & Risk Alignment** guide.")
            st.success("##### 1. Correct Risk Classification")
            st.markdown("Using the **Multi-Factor Risk Calculator**, they correctly identify the system as **High-Risk** due to its high impact on educational access. This immediately triggers a formal set of controls.")

            st.success("##### 2. Law is Translated to Code")
            st.markdown("Using the **Regulatory Mapping Framework**, the Product Owner translates the 'Human Oversight' requirement into a specific user story: *\"As an admissions officer, I want to view the top 5 factors for each AI score so I can make an informed final decision.\"*")

            st.success("##### 3. An Audit Trail is Created")
            st.markdown("The team uses the **Compliance Addendum Template**. As they complete their data bias audit, the results are automatically linked in the Data Governance Log section. This creates a real-time, defensible record of their due diligence.")

            st.info("**Result:** The guide provides a clear, structured process. The final system is not only compliant by design but also has a comprehensive audit trail to prove it, satisfying regulators and building trust with applicants.")

    st.markdown("---")

    # --- 7. Bibliography and Further Reading ---
    st.subheader("📚 Further Reading & Bibliography")
    with st.expander("Expand to see key resources for the Regulatory Compliance & Risk Alignment Toolkit"):
        st.markdown("""
        Navigating the complex, fast-evolving landscape of AI regulation requires grounding in both legal and technical scholarship. These resources provide the foundation for the risk-based, integrated compliance approach of this toolkit.

        ##### Foundational Readings on AI Regulation & Governance:

        - **Veale, M., & Zuiderveen Borgesius, F. (2021). *Demystifying the Draft EU Artificial Intelligence Act.***
          - **Why it's important:** A clear, accessible overview of the structure and core principles of the EU AI Act. This is the best starting point for understanding the risk-based tiers and high-risk requirements that drive this toolkit's compliance framework.
        
        - **Wachter, S., et al. (2017). *Why a right to explanation of automated decision-making does not exist in the General Data Protection Regulation.***
          - **Why it's important:** Despite its title, this paper provides one of the most insightful analyses of what GDPR Article 22 *does* require, focusing on "meaningful information about the logic involved" rather than a full technical explanation. It informs the design of transparency and explainability controls.
        
        - **Bradford, A. (2020). *The Brussels Effect: How the European Union rules the world.***
          - **Why it's important:** Explains the global significance of EU regulations like the AI Act and GDPR. This work provides the strategic context for why organizations outside the EU must still pay close attention to these rules, justifying the investment in compliance.

        ##### On Specific Toolkit Components:

        - **For Risk Classification:** **Selbst, A. D. (2020). *The Danger of Bounding rectangles: A Critical Look at Algorithmic Risk Assessments.***
          - **Why it's important:** This work (and related papers by Selbst) critiques simplistic risk assessments and argues for a more sociotechnical approach. It motivates the multi-factor, context-aware risk calculator in this toolkit.
        
        - **For Evidence & Audit Trails:** **Raji, I. D., et al. (2020). *Closing the AI accountability gap...***
          - **Why it's important:** Essential reading for understanding the need for systematic, end-to-end audit trails. This paper's framework for internal auditing provides the conceptual backbone for the "Evidence Collection" and "Compliance Addendum" templates.
        
        - **For Translating Law to Code:** **Kaminski, M. E., & Malgieri, G. (2021). *Algorithmic impact assessments under the GDPR...***
          - **Why it's important:** Provides a detailed analysis of how to translate the legal requirements of GDPR's impact assessments into concrete, multi-layered explanations and technical documentation, directly informing the "Translating Law to Code" section.
        """)


# --- PART 5: FULL PLAYBOOK & SYNTHESIS ---
with part5:
    st.header("Part 5: Full Playbook & Synthesis 🧩")
    st.info(
        "**Objective:** To integrate the four previous components into a single, cohesive deployment methodology. This section provides a clear, end-to-end workflow, an implementation guide, and frameworks for validation and adaptation, enabling organizations to deploy fairness practices at scale."
    )
    st.markdown("---")

    # --- 1. The Integrated Workflow ---
    st.subheader("🔄 The Integrated Workflow: How It All Connects")
    st.markdown("This workflow shows how outputs from each part of the playbook feed into the others, creating a continuous cycle of compliant, governed, and fair AI development.")
    
    
    with st.expander("See a step-by-step breakdown of the workflow"):
        st.markdown("""
        1.  **Project Inception & Risk Classification (Part 4):** A new AI project begins. The first step is to use the **Risk Classification Calculator** from the *Regulatory Compliance Guide* to determine if the system is low, high, or unacceptable risk.
        2.  **Governance Activation (Part 2):** A "High-Risk" classification immediately engages the *Organizational Integration Toolkit*. The **AI Review Board** is notified and becomes the designated governance gate for the project.
        3.  **Agile Team Setup (Part 1):** The development team adopts the *Fair AI Scrum Toolkit*. Guided by the regulatory needs (**Part 4**) and governance policies (**Part 2**), the Product Owner writes fairness-aware user stories with clear, measurable acceptance criteria.
        4.  **Technical Implementation (Part 3):** During sprints, developers consult the *Advanced Architecture Cookbook* to select the appropriate technical "recipe" needed to meet the fairness requirements of their user story (e.g., implementing disaggregated performance analysis for a computer vision model).
        5.  **Documentation & Audit Trail (Parts 2 & 4):** As part of their **Definition of Done (Part 1)**, the team must complete the **Fairness Impact Statement (Part 2)** and the **Compliance Addendum (Part 4)**. This creates the mandatory audit trail.
        6.  **Governance Gate Review (Part 2):** Before deployment, the completed documentation is formally submitted to the **AI Review Board**. They review the evidence and make a go/no-go decision, fulfilling the governance control triggered in step 2.
        7.  **Deployment & Continuous Monitoring:** The system is deployed. The process loops back as new features are developed or as monitoring reveals the need for fairness adjustments.
        """)

    st.markdown("---")

    # --- 2. End-to-End Case Study ---
    st.subheader("🏢 End-to-End Case Study: Multi-Team AI Recruitment Platform")
    st.markdown("This case study demonstrates the application of the full, integrated playbook to prevent the siloed failures seen in previous examples.")

    st.markdown("""
    A company is building a large-scale AI recruitment platform with three teams: Team A (Sourcing), Team B (Matching), and Team C (Interview Analysis).

    - **Step 1: Risk Classification (Part 4):** The system, which impacts employment opportunities, is immediately classified as **High-Risk** under the EU AI Act framework.
    - **Step 2: Governance Setup (Part 2):** This classification triggers the formation of an **AI Review Board**. A **Fairness Champion** with expertise in HR systems is assigned to oversee the three teams.
    - **Step 3: Team Implementation (Part 1):** All three teams adopt **Fair AI Scrum**. Team A's Product Owner writes a user story to "screen candidates... while ensuring equal opportunity for selection across racial groups."
    - **Step 4: Technical Solution (Part 3):** Team A consults the **Cookbook** and uses the "Disaggregated Performance Analysis" recipe for their classification model. Team C, working on video analysis, uses a combination of recipes for LLMs (transcript analysis) and Vision (facial attribute analysis).
    - **Step 5: Integrated Documentation & Review (Parts 2 & 4):** Before their component can be deployed, each team must complete and link their **Fairness Impact Statement** and **Compliance Addendum**. The AI Review Board holds a formal gate review, assessing the *entire chain* of components to check for compounding biases. They approve the system for a pilot launch only after Team C demonstrates acceptable performance for non-native English speakers.

    **Result:** The integrated playbook creates a unified, legally sound, and technically rigorous process. It prevents inconsistent standards and ensures clear accountability, transforming a high-risk project into a defensible and demonstrably fairer system.
    """)
    st.markdown("---")

    # --- 3. Validation Framework ---
    st.subheader("✅ Validation Framework: How to Measure Success")
    st.markdown("This framework provides guidance for verifying the effectiveness of your playbook implementation, using both leading (process) and lagging (outcome) indicators.")

    col1, col2 = st.columns(2)
    with col1:
        st.info("#### Process Metrics (Leading Indicators)")
        st.markdown("""
        - **Adoption Rate:** Percentage of user stories for high-risk features that include fairness criteria. (Target: 100%)
        - **Task Completion:** Completion rate of fairness-specific tasks compared to functional tasks within sprints. (Target: >95%)
        - **Team Engagement:** Frequency of "fairness blockers" being raised and resolved in daily standups.
        """)

    with col2:
        st.warning("#### Outcome Metrics (Lagging Indicators)")
        st.markdown("""
        - **Reduced Harm:** A measurable reduction in fairness-related incidents or complaints discovered post-deployment.
        - **Improved Equity:** Demonstrable improvement in fairness metrics (e.g., parity scores) in deployed systems.
        - **Increased Efficiency:** Decrease in the time required to address and mitigate identified bias issues.
        - **Compliance Success:** Zero high-severity fairness issues reaching production and successful completion of internal or external audits.
        """)

    st.markdown("---")

    # --- 4. Adaptability Guidelines ---
    st.subheader("🌐 Adaptability Guidelines")
    st.markdown("The playbook is a flexible framework, not a rigid set of rules. Here's how to adapt it across different domains and problem types.")

    with st.expander("Adapting by Industry Domain"):
        st.markdown("""
        - **Healthcare:** Place the highest emphasis on **Risk Classification (Part 4)**, as most systems will be high-risk. The **Governance Body (Part 2)** must include clinical experts and bioethicists. Protected groups may include specific patient populations with rare conditions.
        - **Finance:** Focus heavily on the **Regulatory Compliance Guide (Part 4)** to align with fair lending laws (e.g., ECOA). The **Audit Trail** and documentation templates are critical for demonstrating compliance to regulators. Explainability recipes from the **Cookbook (Part 3)** are essential.
        - **E-commerce:** The key challenge is often fairness of exposure in **Recommendation Systems (Part 3)**. The **Governance Body (Part 2)** should focus on defining what constitutes "fair" exposure for sellers or products (e.g., promoting small businesses).
        """)

    with st.expander("Adapting by AI Problem Type"):
        st.markdown("""
        - **Classification:** The playbook's examples are well-suited for this. Focus on metrics like equal opportunity, predictive parity, and disaggregated accuracy.
        - **Regression:** Adapt fairness definitions to focus on error disparities. A key question is: "Is the model's prediction error (e.g., over- or under-estimating a price) significantly larger for one group than another?"
        - **Generative AI (LLMs, Image Models):** Rely heavily on the **Advanced Architecture Cookbook (Part 3)** for specialized recipes on stereotype testing, toxicity evaluation, and preventing harmful content generation. The **Governance (Part 2)** must define policies on acceptable use and content.
        """)
        
    st.markdown("---")

    # --- 5. Future Iterations ---
    st.subheader("🔮 Future Iterations: How This Playbook Can Evolve")
    st.markdown("An effective fairness strategy is a living process. Here are potential improvements for future versions of this playbook:")
    st.markdown("""
    - **Deeper MLOps Integration:** Developing plugins and automated checks that integrate directly into CI/CD pipelines, flagging potential fairness issues on every code commit.
    - **Expanded Cookbook:** Adding more recipes to the **Architecture Cookbook** for emerging technologies like Graph Neural Networks and Reinforcement Learning systems.
    - **Automated Documentation:** Creating tools that automatically populate sections of the **Fairness Impact Statement** and **Compliance Addendum** based on code analysis and model evaluation results, reducing developer burden.
    - **Dynamic Risk Assessment:** Moving from a static, upfront risk assessment to a dynamic model that re-evaluates risk throughout the AI lifecycle as the system is used in new contexts.
    """)

    st.markdown("---")

    # --- 6. Bibliography and Further Reading ---
    st.subheader("📚 Further Reading & Bibliography")
    with st.expander("Expand to see key resources for the Full Playbook & Synthesis"):
        st.markdown("""
        This section synthesizes all previous parts into a cohesive whole. The key challenge is creating a practical, integrated workflow. While many papers focus on specific components, the following resources discuss the broader challenge of end-to-end integration and evaluation.

        *(Note: The citations in the original text for this section were numerical and could not be resolved. The following are suggested foundational readings for the topics of integration, validation, and adaptation.)*

        ##### Foundational Readings on Integrated AI Governance:

        - **Raji, I. D., et al. (2020). *Closing the AI accountability gap: Defining an end-to-end framework for internal algorithmic auditing.***
          - **Why it's important:** This paper is arguably the most influential work on creating an integrated, end-to-end process for AI accountability. The workflow presented in this playbook is heavily inspired by the lifecycle approach detailed in this research.
        
        - **Smuha, N. A., et al. (2023). *How to operationalize AI regulation...***
          - **Why it's important:** This paper directly tackles the challenge of "operationalizing" regulation, which is the core goal of the integrated playbook. It discusses the practical difficulties of connecting legal requirements to technical work, motivating the need for a comprehensive methodology.

        ##### On Validation and Measurement:

        - **Saleiro, P., et al. (2018). *Aequitas: A Bias and Fairness Audit Toolkit.***
          - **Why it's important:** While this playbook is process-focused, validation depends on robust tools. Aequitas is an open-source tool that provides a practical foundation for generating the "Outcome Metrics" needed for the validation framework.
        
        - **Weidinger, L., et al. (2022). *Taxonomy of risks posed by language models.***
          - **Why it's important:** For adapting the playbook to new domains, especially those involving generative AI, a structured understanding of potential harms is crucial. This taxonomy provides a framework for identifying the risks that your adapted playbook will need to address.
        """)
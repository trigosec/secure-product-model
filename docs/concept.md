# Introduction to the Secure Product Control Framework
The Secure Product Control Framework is designed specifically for engineering and technology teams. Unlike traditional control frameworks, which are often abstract or high level, this framework is structured to provide actionable and practical guidance directly aligned with how technology organizations operate.
The framework is built around three core elements: Resources, Governance, and Controls. Together, these elements support a clear and structured approach to implementing regulatory requirements, managing risk, and ensuring operational consistency.
## 1. Resources
Resources are the foundational elements that are subject to control and oversight. These include items that can be cataloged or inventoried, such as:
- Suppliers and service providers
- Internal systems and applications
- Code repositories
- Environments (e.g., production, staging)

Resources define the scope of what is being managed. They serve as the “objects” that controls and governance processes act upon. For example, a regulation might require maintaining an inventory of all third-party providers, which would fall under this category.
## 2. Governance
Governance defines how resources and controls are managed over time. This includes:
- Policies
- Review cycles
- Scoping documents, like the description of the locations in which the business operates.
- Approval processes

Governance ensures consistency and accountability. It provides the structure that keeps controls effective and aligned with business and regulatory expectations.
## 3. Controls
Controls are the specific actions, checks, or validations that must be performed. These are typically measurable or testable, and they serve as the operational implementation of governance. Examples include:
- Ensuring access reviews are performed quarterly
- Validating that all production systems have backup procedures
- Verifying that supplier assessments are completed before onboarding

Each control is linked to one or more resources and governed through defined policies and review mechanisms.
## Purpose of this framework
The purpose of this framework is to translate regulatory and governance expectations into a structure that is meaningful and actionable for technology teams. Traditional control frameworks often fall short in engineering environments because they lack specificity and practical relevance. This framework addresses that gap by defining clear, concrete elements (resources, governance, and controls) that map directly to how technology organizations operate.
By organizing responsibilities and expectations into these three components, the framework enables teams to:
- Identify what needs to be managed (resources)
- Establish how it should be managed (governance)
- Apply and test the required practices (controls)

This practical approach improves accountability, reduces ambiguity, and supports better alignment between compliance, risk, and technical execution.
## Notes
I am currently mapping the framework to PCI DSS v4.0.1 (~90% complete). My objective is to map it to ISO 27001, DORA, SOC2, NIS2 and MiCA. This list will grow as I expand the scope.
### Approach to market (WIP)
My plan is to make the controls public and I will build the developer tooling around these. As an example, let’s say that a developer is building network infrastructure, they can then look it up online and also use the tool to guide them in the process to secure it. Later they will integrate this same tool in their CI/CD pipeline to validate that infrastructure is still compliant as they continue developing it.

Mappings to standards and regulations would be accessible through a fee. I have to decide on the billing model (1-off vs recurring). I will be following new regulations and as they come up I will add the mapping. This would help teams using this framework, to trace compliance and have automated gap analysis.

I intend to use the Governance elements of the framework as value added. Let’s say that you are updating the Business Continuity Policy and you would like to verify that it complies with DORA and ISO 27001. Through the mapping I will present to you the relevant sections of the regulation/standard and then provide a first draft using Gen AI. You still need to make it yours, but it should alleviate the efforts.

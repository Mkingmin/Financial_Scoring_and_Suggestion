# Preface
Financial Scoring & Suggestion is a mock project that employs machine learning technique to deliver the solution for CLV improvement in Fintech industry. The main purpose of that mock project is to indicate the process of solution development and delivery that I use as a Business Analyst. <br>
<br>Are you now ready to explore the solution? Read the full flow of idea and check out models. Let's start!
# Executive summary
As the demand for financial products continues to rise, financial enterprises are grappling with **a surge in rejected applications** for financial products and credit, resulting in **decreased Customer Lifetime Value (CLV)**. The **root cause** of this problem is _the discrepancy between customer needs and financial capabilities_. Given the customer insights that reveal customers are tech-savvy, prioritize digital solutions, and expect time-efficient experiences, the **Financial Scoring & Suggestion solution** emerges as the most effective solution, enabling quick assessment of customers' financial capabilities and automatic recommendation of suitable financial products.<br>
![image](https://github.com/user-attachments/assets/11b25f00-3943-4a99-b117-02dba557deb7)
<br>
_Executive summary of Financial Scoring mock project_
# Problem (Inital Problem)
The CLV (Customer Lifetime Value) decreases for digital financial and credit enterprises. Efforts in customer service have increased, but the results are not significant.

# Solution development
In the solution development stage, I use **Double Diamond framework**, which switches respectively between **Divergence** (open, innovative status) and **Convergence** (focus, strategic status) in order to define root cause of the problems and create the best solution to resolve the root cause. I go through 4 phases to develop the disruptive and appropriate solution:
- Discover phase
- Define phase
- Develop phase
- Deliver phase
![Initial Double Diamond framework](https://github.com/user-attachments/assets/a8c59dcb-3afc-4144-b929-e724da9ea3c0)
<br> _Double Diamond framework that is employed to develop solution_

## 1. Dicover phase
Discover phase is the divergent phase, which information and findings of analysis are out of the box collected.
### 1.1. Elicit information from partners (BFSI enterprises)
> **Note**: The information analyzed below is based on real story from financial partners I have had the opportunity to collaborate with. For confidentiality reasons, I would like to refrain from providing specific figures and will not disclose the names of the individuals or organizations involved.

**Summary 1**: BFSI enterprises say that they have been suffered the decline in value per customer, which is the result of the decrease of value per transaction and the huge number of customer's applications that are rejected _(over 40% registration for financial and credit products are unqualified per month)._
<br><br> Factors that lead customers to be rejected are:
- **The discrepancy between customer needs and financial capabilities**, which means they register in financial products that have higher standards than their capabilities
- **Incorrect information during the registration process**

### 1.2. Customer demands analysis
**Summary 2:** Negative emotion from the previous experience can lead to the significant decrease in customer retention rate
<br> There are some noteworthy insights about customers in financial industry:
- 73% of consumers will switch to a competitor after multiple bad experiences - both UI, UX and customer service experiences (Zendesk, 2024, [51 customer service statistics you need to know](https://www.zendesk.com/blog/customer-service-statistics/#) )
- More than half of consumers will switch to a competitor after only one bad experience (Zendesk, 2024, [51 customer service statistics you need to know](https://www.zendesk.com/blog/customer-service-statistics/#) )
- Timely disbursement positively affects to retention rate of customers in loan category (Craig Churchill, 2000, [Banking on Customer Loyalty](https://scholarsarchive.byu.edu/esr/vol2/iss2/2/) )

### 1.3. Competitive analysis
> **Objective:** Competitive analysis is conducted in order to explore which aspects financial enterprises focusing their investments on and which aspects the enterprises are excelling in.

**Summary 3:** The digital financial market is experiencing intense competition as most companies are intensifying their investments to enhance user experience on mobile applications and websites, while also ramping up promotional and marketing activities.
<br><br> Analyzing Strategy map of BFSI enterprises to discover their strategy and value curve
<br> ![image](https://github.com/user-attachments/assets/a3eeed8b-e1d5-4763-b799-401c67709d65)
<br>_Strategy map of BFSI industry_
<br>
<br> The above strategy map and value curve represents for 7 competing factors which are the key factors that customers consider when making purchasing decisions. These key factors:
<ul>
  <li>Diversity of product categories</li>
  <li>Personalization</li>
  <li>User experience on application, website</li>
  <li>User interface on application, website</li>
  <li>Time of disbursement</li>
  <li>Promotional and marketing activities</li>
  <li>Diversity and uniqueness of the feature on application, website</li>
</ul>

Financial enterprises are following the differentiation strategy. Customer experience factors, user interface on applications and websites, and promotional activities are areas that these financial companies are focusing their investments on, creating fierce competition in this field.
## 2. Define phase
Let's move on to **Convergent status** where we focus and structure all of the findings in the **Discover phase** above to define the right core problem (or root cause)
<br><br>**Root cause:** The discrepancy between customer needs and financial capabilities
<br>
![image](https://github.com/user-attachments/assets/93e2bc33-0c88-48eb-bcd3-bf53a48c13d5)
<br> _Issue tree to find out root causes from the Inital problem_
<br><br> Although we have some root causes such as slow loading speed, non-diverse functions, lack of promotion, and slow disbursement, these root causes are situated within a highly competitive area mentioned in section [1.3. Competitive analysis](https://github.com/Mkingmin/financial-scoring-mock-project/blob/main/README.md#13-competitive-analysis). Focusing on addressing these root causes with the goal of surpassing competitors is not a viable or cost-efficient option. Instead, the root cause of the incompatibility between customer needs and financial capabilities is the core problem that most competitors have yet to address. If we focus to solve this root cause (or core problem), the opportunity to regain CLV and increase competitive advantage over other enterprises is greater.
<br><br> **Problem statement:** "The discrepancy between customer needs and financial capabilities" is the core problem, which, if solved, promises not only to resolve the initial problem but also to bring competitive advantages with optimized costs and promising ROI.
## 3. Develop phase
> This is the divergent phase - open to find out and dive deep into all of the relevant materials and innovative approaches for solution. Focusing on customer behavior analysis and opportunity analysis is the way to shed light on insights and market gap
### 3.1. Customer insights
#### Demographic
Demographic characteristics of target customer include:
- Age: 18 - 35
- Income: >= 5 mil VND per month
#### Behavior
- Prioritize time efficient solution because they are busy, which is 76% of customers say they expect to engage with someone immediately when contacting a company (Michael Keenan, 2023, [Fast Customer Service: An Easy Way to Improve Your Retail Business](https://www.shopify.com/ph/enterprise/blog/fast-customer-service))
- Tech savvy generation who prefers digital solution than traditional customer service as tele-sales, which 75% of Gen Z are more likely to buy a product if they can customize it online before purchasing (Wpengine, 2020, [Generation Influence: Reaching Gen Z in the New Digital Paradigm](https://wpengine.com/resources/gen-z-2020-full-report/))
#### Psychology
- Successful disbursement capability is the most important thing for users
- Lose trust and churn if experienced multiple rejections
- Be open in sharing information to receive a better experience
### 3.2. Opportunity analysis
As analyzed in [Section 1.3](https://github.com/Mkingmin/financial-scoring-mock-project/blob/main/README.md#13-competitive-analysis), digital BFSI competitors are investing heavily in user experience, user interface, and promotion, thereby gaining a certain edge. By addressing customer satisfaction through a reduction in application cancellation rates, new opportunities below may arise:
- Transcending the intense competition in the digital BFSI industry category
- Minimizing customer service costs and efforts, to allocate resources more efficiently elsewhere
## 4. Deliver phase
> This is the divergent phase - synthsize and structure all findings on Develop phase above

![image](https://github.com/user-attachments/assets/84dca345-2d63-43f5-bab1-ac1d53c7eef5)
<br> _Financial scoring & suggestion solution development_
<br><br>
**Solution statement:** Financial Scoring & Suggestion is an innovative solution that streamlines the financial product recommendation process by automatically evaluating user's financial capability and suggesting relevant products. This not only enhances the user satisfaction by matching them with suitable financial products to reduce application cancellations and ultimately boosts Customer Lifetime Value (CLV), but also minimizes customer service costs.

## Solution summary
![image](https://github.com/user-attachments/assets/213f0e59-2a82-42c2-906c-e68d01f7d8e3)
<br> _Completed Double Diamond framework. Read details [here]()_
# Executive plan
## Technology (machine learning algorithms that are employed)
- **Applying Decision tree algorithm**: CART (Classification and Regression Tree) in particular
- **Objectives of each algorithm**: CART (Classification and Regression Tree) is used to evaluate financial capability of customers based in the specific criteria
## CART (Classification and Regression Tree) algorithm
### Data preparation
Dataset that has been employed in that model is the sample dataset about credit card which includes in Econometric Analysis book (check out for more about Econometric Analysis book [here](https://archive.org/details/econometricanaly0000gree_f5q0/mode/2up)). The reason I choose that dataset to train and test the CART model is its fit with the business logic. Because the dataset is sample dataset, so it's clean and makes no need for cleaning or handling missing values.
<br> <br> `df= pd.read_csv('AER_credit_card_data.csv')
df.head()`
<br><br> ![image](https://github.com/user-attachments/assets/5c86140b-d0d1-4628-a7c2-79257fc6a2dc)
### Modelling
Being approved or rejected for a credit card is considerd as a measure of a customer's financial capability, because credit cards have the highest approval standards and also have the highest rejected rate.
![image](https://github.com/user-attachments/assets/079b98a6-d60a-46b6-87a6-68808f417051)
<br> _Business logic of CART model_
#### Building CART model
**- Target variable:** 'card' - whether a customer is approved for a credit card or not
<br> **- Feature selection:** 'reports', 'age', 'income', 'share', 'expenditure', 'owner', 'selfemp', 'majorcards', 'active' is the list of features that impact credit card approval rates for customers
<br> Model building and visualizing
<br> ![decision_tree_plot](https://github.com/user-attachments/assets/6245a14e-bc5b-4323-94ca-e948256a89d6)
<br> _Visualization of model_
<br> That model use Gini ratio as the Attribute Selection Measures, which measures the impurity of the node
#### Evaluating model
`print("Accuracy:",metrics.accuracy_score(y_test, y_pred))`
<br><br>
<img src="https://github.com/user-attachments/assets/8917ddac-b9eb-4bc4-80a9-9bb6fdc9b76b" width="500">
#### Optimizing model
With the Accuracy value 0.96, which means the predict value has 96% probability to equal to actual value. Therefore, we don't need to optimize the model
### Suggestion
Based on the predict result of CART model, if the user is predicted to belong to the **Potential customer group** (i.e., those who have been approved for a credit card), the system will automatically suggest financial products with high value and stringent approval conditions for them, such as credit cards and personal loans. On the other hand, if the user is predicted to belong to the **Risky customer group** (i.e., credit card applications are rejected), they will be suggested products with low value and simple approval conditions, such as payment cards. This helps users to register for products that match their financial capabilities, reducing the rate of rejected applications.

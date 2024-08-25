# Model from Hugging Face hub
base_model = "NousResearch/Llama-2-7b-chat-hf"
# Fine-tuned model save directory
save_dir = "model"

####### System prompt
example_input = {
    "text": "SECTION 1. SHORT TITLE. This Act may be cited as the ``Boosting Equity for the American Middle Class Act of 2016'' or as the ``BEAM Act of 2016''. SEC. 2. REFUNDABLE CREDIT FOR EARLY PRINCIPAL PAYMENTS ON CERTAIN HOME MORTGAGES. (a) In General.--Subpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 36B the following new section: ``SEC. 36C. EARLY PRINCIPAL PAYMENTS ON CERTAIN HOME MORTGAGES. ``(a) In General.--In the case of an individual, there shall be allowed as a credit against the tax imposed by this subtitle for the taxable year an amount equal to 50 percent of the excess home mortgage principal payments made by the taxpayer during such taxable year. ``(b) Annual Dollar Limitation.--The credit allowed under subsection (a) with respect to any taxpayer for any taxable year shall not exceed $500. ``(c) Lifetime Limitation.--No credit shall be allowed under subsection (a) to any taxpayer for any taxable year if credit was allowed under subsection (a) to such taxpayer for any 10 preceding taxable years. ``(d) Limitation Based on Modified Adjusted Gross Income.-- ``(1) In general.--The amount which would (but for this paragraph and after the application of subsection (b)) be allowable as a credit under subsection (a) shall be reduced (but not below zero) by the amount which bears the same ratio to the amount which would be so allowable as-- ``(A) the excess of-- ``(i) the taxpayer's modified adjusted gross income for the taxable year, over ``(ii) $125,000 (twice such amount in the case of a joint return), bears to ``(B) $10,000 (twice such amount in the case of a joint return). ``(2) Modified adjusted gross income.--The term `modified adjusted gross income' means adjusted gross income increased by any amount excluded from gross income under section 911, 931, or 933. ``(e) Excess Home Mortgage Principal Payments.--For purposes of this subsection-- ``(1) In general.--The term `excess home mortgage principal payments' means, with respect to qualified home mortgage indebtedness for any taxable year, the excess of-- ``(A) the aggregate amount of principal paid by the taxpayer with respect to such indebtedness during such taxable year, over ``(B) the aggregate amount of principal which would have been paid by the taxpayer with respect to such indebtedness during such taxable year if the taxpayer had timely made each required payment under the terms of the indebtedness during such taxable year (and no other payments). ``(2) Qualified home mortgage indebtedness.-- ``(A) In general.--The term `qualified home mortgage indebtedness' means any acquisition indebtedness (as defined in section 163(h)(3)(B)) if-- ``(i) the residence with respect to such acquisition indebtedness is the primary residence (within the meaning of section 121) of the taxpayer, and ``(ii) such indebtedness constitutes a traditional mortgage. ``(B) Traditional mortgage.--For purposes of this paragraph, the term `traditional mortgage' means indebtedness-- ``(i) the term of which is not less than 15 years and not more than 30 years, and ``(ii) the required payments under which are each the same amount and made in equal intervals during the term of the indebtedness (or if any payment is required at a different interval, the amount of such payment is adjusted in the same proportion as the change in interval). ``(f) Rules Related to Joint Returns.-- ``(1) No credit for married individuals filing separately.--In the case of a married individual, no credit shall be allowed under this section for any taxable year unless such individual files a joint return with such individual's spouse for such taxable year. ``(2) Application of lifetime limitation with respect to joint returns.--If the credit under subsection (a) is allowed with respect to a joint return for any taxable year, such credit shall be treated for purposes of applying subsection (c) as allowed to both spouses for such taxable year. For purposes of applying subsection (c) with respect to a joint return for any taxable year, the taxpayer shall be treated as having been allowed the credit under subsection (a) for 10 or more preceding taxable years only if both spouses have been so allowed such credits.''. (b) Reporting of Excess Home Mortgage Principal Payments.--Section 6050H(b)(2) of such Code is amended by striking ``and'' at the end of subparagraph (C), by redesignating subparagraph (D) as subparagraph (E), and by inserting after subparagraph (C) the following new subparagraph: ``(D) the amount of excess home mortgage principal payments (as defined in section 36C(e)) received with respect to such mortgage during the calendar year, and''. (c) Conforming Amendments.-- (1) Section 6211(b)(4)(A) of such Code is amended by inserting ``36C,'' after ``36B,''. (2) Section 1324(b)(2) of title 31, United States Code, is amended by inserting ``36C,'' after ``36B,''. (3) The table of sections for subpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 36B the following new item: ``Sec. 36C. Early principal payments on certain home mortgages.''. (d) Effective Date.--The amendments made by this section shall apply to taxable years ending after the date of the enactment of this Act."
}
example_output = "Boosting Equity for the American Middle Class Act of 2016 or the BEAM Act of 2016 This bill amends the Internal Revenue Code to allow a refundable tax credit equal to 50% of the excess home mortgage principal payments made by a taxpayer during the year. The credit is limited to $500 per year and to taxpayers who have not received the credit for any of the 10 preceding years. The bill reduces the amount of the credit for taxpayers with modified adjusted gross incomes above specified levels. An &quot;excess home mortgage principal payment&quot; is the excess of: (1) the amount of principal paid by the taxpayer with respect to a mortgage during the year, over (2) the amount of principal the taxpayer would have paid by making each required payment on a timely basis under the terms of the mortgage (and no other payments). The mortgage must: (1) be for a primary residence, (2) for a term between 15 and 30 years, and (3) require payments that are each the same amount and made in equal intervals during the term of the mortgage (or if any payment is required at a different interval, the amount of the payment is adjusted in the same proportion as the change in interval). Married individuals must file a joint tax return to claim the credit. Persons engaged in a trade or business (e.g., lenders, mortgage companies, or banks) who are required to report mortgage interest payments from individuals of $600 or more must also report the amount of excess home mortgage principal payments received during the year."

input_format = {
    "text": "XXX"
}
system_prompt = f"""
You are an expert in the art of summarization. Given a document or passage of text, generate a concise and coherent summary that captures the key information, main ideas, and important details. Ensure that the summary is well-structured, informative, and retains the original context. 
Focus on preserving the nuance and tone of the original text while delivering a condensed version that is easily comprehensible. 
Consider potential use cases such as news articles, research papers, and informative blog posts. Strive for accuracy, clarity, and conciseness in your summarization output.

The input will be a json delimited by triple hashtags in the following format:

###
{input_format}
###

Example:
Input:
###
{example_input}
###
Output: {example_output}
"""
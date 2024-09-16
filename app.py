import streamlit as st
import matplotlib.pyplot as plt

# Brief Explanation of CVP Analysis
st.title("Cost-Volume-Profit (CVP) Analysis for Smartfoods")
st.write("""
### Cost-Volume-Profit (CVP) Analysis Overview:
CVP analysis helps you understand how changes in costs and sales volume affect profitability. The goal is to determine the break-even point and the volume of sales needed to achieve a target profit.

**Key Terms:**
1. **Contribution Margin**: The amount left after deducting variable costs from sales revenue. It contributes to covering fixed costs and generating profit.  
   - Formula: Contribution Margin = Sales Price per Unit - Variable Cost per Unit

2. **Break-even Point**: The sales volume where total revenue equals total costs (no profit or loss).  
   - Formula: Break-even Sales Volume = Fixed Costs / Contribution Margin

3. **Target Profit**: The sales volume required to achieve a specific profit goal.  
   - Formula: Target Sales Volume = (Fixed Costs + Target Profit) / Contribution Margin
""")

# Section 1: CVP Analysis for Normal Sales Cycle (No WhatsApp Promotions)
st.subheader("Section 1: CVP Analysis for Normal Sales Cycle (No WhatsApp Promotions)")

# Inputs for normal sales cycle with placeholders set to zero
fixed_costs = st.number_input("Fixed Operating Costs (ZAR)", min_value=0.0, value=0.0)
variable_cost_per_unit = st.number_input("Variable Cost per Basket (Average Variable Cost per Meal, ZAR)", min_value=0.0, value=0.0)
avg_basket_value = st.number_input("Average Basket Value (Average Meal Value, ZAR)", min_value=0.0, value=0.0)
target_profit = st.number_input("Target Profit (Total Profit Goal, ZAR)", min_value=0.0, value=0.0)

# Contribution Margin Calculation
contribution_margin = avg_basket_value - variable_cost_per_unit

# Check for invalid contribution margin
if contribution_margin <= 0:
    st.error("Contribution margin is zero or negative. Please ensure that the average basket value is greater than the variable cost.")
else:
    # Calculate break-even and target profit volume
    break_even_volume = fixed_costs / contribution_margin
    target_volume = (fixed_costs + target_profit) / contribution_margin  # Total Profit Goal is used here

    # Calculate revenue for both break-even and total profit goal
    break_even_revenue = break_even_volume * avg_basket_value
    target_profit_revenue = target_volume * avg_basket_value

    # Display calculated values
    st.success(f"Break-even volume: {break_even_volume:.2f} baskets")
    st.success(f"Volume to achieve total profit goal: {target_volume:.2f} baskets")
    st.success(f"Total revenue to achieve profit goal: ZAR {target_profit_revenue:,.2f}")

    # Plot the graph for break-even and target profit
    st.write("### Break-even and Total Profit Goal Visualization (Normal Sales Cycle)")
    
    volumes = range(0, int(target_volume) + 100)
    total_costs = [fixed_costs + (variable_cost_per_unit * v) for v in volumes]
    sales_revenue = [avg_basket_value * v for v in volumes]

    fig, ax = plt.subplots()
    ax.plot(volumes, total_costs, label='Total Costs (Fixed + Variable)', color='red')
    ax.plot(volumes, sales_revenue, label='Sales Revenue', color='green')
    ax.axhline(fixed_costs, color='blue', linestyle='--', label='Fixed Costs')

    # Break-even line
    ax.axvline(break_even_volume, color='black', linestyle='--', alpha=0.6)
    ax.axhline(break_even_revenue, color='black', linestyle='--', alpha=0.6)
    ax.plot([break_even_volume, break_even_volume], [0, break_even_revenue], linestyle='--', color='black', alpha=0.6)

    # Target profit line with correct placement
    ax.axvline(target_volume, color='orange', linestyle='--', alpha=0.6)
    ax.axhline(target_profit_revenue, color='orange', linestyle='--', alpha=0.6)
    ax.plot([target_volume, target_volume], [0, target_profit_revenue], linestyle='--', color='orange', alpha=0.6)

    # Adjust y-axis in tens of thousands of ZAR
    ax.set_yticklabels([f'{int(tick / 1000):,}k ZAR' for tick in ax.get_yticks()])

    ax.set_xlabel('Sales Volume (Baskets)')
    ax.set_ylabel('Amount (ZAR)')
    ax.set_title('Cost-Volume-Profit Analysis (No WhatsApp Promotions)')
    ax.legend()

    st.pyplot(fig)

    # Section 2: CVP Analysis Including WhatsApp Promotions
    st.subheader("Section 2: CVP Analysis with WhatsApp Promotions")

    # Inputs for WhatsApp Promotions (Placeholders set only for delivery rate and conversion rate)
    whatsapp_messages_sent = st.number_input("Number of WhatsApp Messages Sent", min_value=0, value=0)
    delivery_rate = st.slider("Delivery Rate (%)", min_value=0.0, max_value=100.0, value=85.0) / 100
    conversion_rate = st.slider("Conversion Rate (%)", min_value=0.00, max_value=10.00, value=2.00) / 100

    # Input for WhatsApp Cost and Promotional Discount
    whatsapp_cost_per_message = st.number_input("Cost per WhatsApp Message (ZAR)", min_value=0.0, value=0.0)
    promotional_discount = st.slider("Promotional Discount (%)", min_value=0.0, max_value=100.0, value=0.0) / 100

    # WhatsApp Promotion Impact
    discounted_basket_value = avg_basket_value * (1 - promotional_discount)
    expected_customers = whatsapp_messages_sent * delivery_rate * conversion_rate
    st.write(f"Number of converted messages: {expected_customers:.2f}")
    expected_sales = expected_customers * discounted_basket_value
    total_marketing_cost = whatsapp_messages_sent * whatsapp_cost_per_message

    # Step 1: Calculate marketing costs (number of messages sent * cost per message)
    marketing_costs = whatsapp_messages_sent * whatsapp_cost_per_message

    # Step 2: Calculate the new grand total (fixed costs + marketing costs + target profit)
    grand_total = fixed_costs + marketing_costs + target_profit

    # Step 3: Calculate the new contribution margin for the discounted WhatsApp-converted customers
    new_contribution_margin = discounted_basket_value - variable_cost_per_unit

    # Contribution from WhatsApp-converted customers
    whatsapp_sales_contribution = expected_customers * new_contribution_margin

    # Step 4: Subtract the WhatsApp contribution from the grand total
    remaining_grand_total = grand_total - whatsapp_sales_contribution

    # Step 5: Calculate the number of regular sales needed using the section 1 (non-discounted) contribution margin
    remaining_sales_needed = remaining_grand_total / contribution_margin if contribution_margin > 0 else 0

    # Total sales is the sum of regular sales + WhatsApp-converted customers
    total_sales = remaining_sales_needed + expected_customers

    # Display updated results for Section 2
    st.success(f"Marketing Costs: ZAR {marketing_costs:.2f}")
    st.success(f"Grand Total (Fixed Costs + Marketing Costs + Target Profit): ZAR {grand_total:.2f}")
    st.success(f"WhatsApp Sales Contribution: ZAR {whatsapp_sales_contribution:.2f}")
    st.success(f"Remaining Grand Total after WhatsApp Sales Contribution: ZAR {remaining_grand_total:.2f}")
    st.success(f"Remaining Regular Sales Needed: {remaining_sales_needed:.2f}")
    st.success(f"Total Sales (Regular + WhatsApp Converted): {total_sales:.2f}")

    # Graph for Section 2
    volumes_with_discount = range(0, int(total_sales) + 100)
    total_costs_with_marketing = [fixed_costs + total_marketing_cost + (variable_cost_per_unit * v) for v in volumes_with_discount]
    sales_revenue_with_discount = [avg_basket_value * remaining_sales_needed + discounted_basket_value * expected_customers for v in volumes_with_discount]

    fig2, ax2 = plt.subplots()
    ax2.plot(volumes_with_discount, total_costs_with_marketing, label='Total Costs (Fixed + Variable + Marketing)', color='red')
    ax2.plot(volumes_with_discount, sales_revenue_with_discount, label='Sales Revenue', color='green')
    ax2.axhline(fixed_costs, color='blue', linestyle='--', label='Fixed + Marketing Costs')

    st.pyplot(fig2)

import streamlit as st
import matplotlib.pyplot as plt

# Section 1: CVP Analysis for Normal Sales Cycle (No WhatsApp Promotions)
st.title("Cost-Volume-Profit (CVP) Analysis for Smartfoods")

# Inputs for normal sales cycle
st.subheader("Section 1: CVP Analysis for Normal Sales Cycle (No WhatsApp Promotions)")
fixed_costs = st.number_input("Fixed Operating Costs (ZAR)", min_value=0.0)
variable_cost_per_unit = st.number_input("Variable Cost per Basket (ZAR)", min_value=0.0)
avg_basket_value = st.number_input("Average Basket Value (ZAR)", min_value=0.0)
target_profit = st.number_input("Target Profit (ZAR)", min_value=0.0)

# Contribution Margin Explanation
st.write("### Contribution Margin Explanation")
st.write("""
The **Contribution Margin** is calculated as the difference between the sales price (average basket value) 
and the variable cost per basket. The formula is:

**Contribution Margin = Sales Price - Variable Cost**

This margin represents how much each sale contributes towards covering fixed costs and, eventually, profit.
""")

# CVP Calculations (Without WhatsApp)
contribution_margin = avg_basket_value - variable_cost_per_unit
if contribution_margin > 0:
    break_even_volume = fixed_costs / contribution_margin
    target_volume = (fixed_costs + target_profit) / contribution_margin
    
    st.write(f"Break-even volume: {break_even_volume:.2f} baskets")
    st.write(f"Volume to achieve target profit: {target_volume:.2f} baskets")

    # Graph for Normal Sales Cycle (No WhatsApp Promotions)
    st.write("### Break-even Point Visualization (Normal Sales Cycle)")
    
    volumes = range(0, int(target_volume) + 100)
    total_costs = [fixed_costs + (variable_cost_per_unit * v) for v in volumes]
    sales_revenue = [avg_basket_value * v for v in volumes]

    fig, ax = plt.subplots()
    ax.plot(volumes, total_costs, label='Total Costs (Fixed + Variable)', color='red')
    ax.plot(volumes, sales_revenue, label='Sales Revenue', color='green')
    ax.axhline(fixed_costs, color='blue', linestyle='--', label='Fixed Costs')
    
    # Highlight the break-even point with a dotted vertical line
    ax.axvline(break_even_volume, color='black', linestyle='--', label=f'Break-even Volume: {break_even_volume:.2f} baskets')
    
    # Adjust y-axis in tens of thousands of ZAR
    ax.set_yticklabels([f'{int(tick / 1000):,}k ZAR' for tick in ax.get_yticks()])
    
    ax.set_xlabel('Sales Volume (Baskets)')
    ax.set_ylabel('Amount (ZAR)')
    ax.set_title('Cost-Volume-Profit Analysis (No WhatsApp Promotions)')
    ax.legend()

    st.pyplot(fig)
    
    # Print breakeven mix
    breakeven_revenue = break_even_volume * avg_basket_value
    st.write(f"To break even, you need to sell {break_even_volume:.2f} baskets with total revenue of ZAR {breakeven_revenue:,.2f}.")

else:
    st.write("Contribution margin is negative. Please adjust input values.")

# Section 2: CVP Analysis Including WhatsApp Promotions
st.subheader("Section 2: CVP Analysis with WhatsApp Promotions")

# Inputs for WhatsApp Promotions
whatsapp_cost_per_message = st.number_input("Cost per WhatsApp Message (ZAR)", min_value=0.0)
delivery_rate = st.slider("Delivery Rate (%)", min_value=0, max_value=100) / 100
conversion_rate = st.slider("Conversion Rate (%)", min_value=0, max_value=100) / 100
whatsapp_messages_sent = st.number_input("Number of WhatsApp Messages Sent", min_value=0)

# WhatsApp Promotion Impact
expected_customers = whatsapp_messages_sent * delivery_rate * conversion_rate
expected_sales = expected_customers * avg_basket_value
total_marketing_cost = whatsapp_messages_sent * whatsapp_cost_per_message

# Updated Break-even Calculations
updated_fixed_costs = fixed_costs + total_marketing_cost
if contribution_margin > 0:
    updated_break_even_volume = updated_fixed_costs / contribution_margin
    updated_target_volume = (updated_fixed_costs + target_profit) / contribution_margin
    
    st.write(f"Updated break-even volume with WhatsApp promotions: {updated_break_even_volume:.2f} baskets")
    st.write(f"Updated volume to achieve target profit: {updated_target_volume:.2f} baskets")
    
    # Graph for WhatsApp Promotion Impact
    st.write("### Break-even Point Visualization (With WhatsApp Promotions)")
    
    total_costs_with_marketing = [updated_fixed_costs + (variable_cost_per_unit * v) for v in volumes]

    fig2, ax2 = plt.subplots()
    ax2.plot(volumes, total_costs_with_marketing, label='Total Costs (Fixed + Variable + Marketing)', color='red')
    ax2.plot(volumes, sales_revenue, label='Sales Revenue', color='green')
    ax2.axhline(updated_fixed_costs, color='blue', linestyle='--', label='Fixed + Marketing Costs')
    
    # Highlight the updated break-even point with a dotted vertical line
    ax2.axvline(updated_break_even_volume, color='black', linestyle='--', label=f'Updated Break-even Volume: {updated_break_even_volume:.2f} baskets')
    
    # Adjust y-axis in tens of thousands of ZAR
    ax2.set_yticklabels([f'{int(tick / 1000):,}k ZAR' for tick in ax2.get_yticks()])
    
    ax2.set_xlabel('Sales Volume (Baskets)')
    ax2.set_ylabel('Amount (ZAR)')
    ax2.set_title('Cost-Volume-Profit Analysis (With WhatsApp Promotions)')
    ax2.legend()

    st.pyplot(fig2)
    
    # Print updated breakeven mix
    updated_breakeven_revenue = updated_break_even_volume * avg_basket_value
    st.write(f"With WhatsApp promotions, you need to sell {updated_break_even_volume:.2f} baskets with total revenue of ZAR {updated_breakeven_revenue:,.2f}.")

else:
    st.write("Contribution margin is negative. Please adjust input values.")

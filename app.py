import streamlit as st
import matplotlib.pyplot as plt

# Section 1: CVP Analysis for Normal Sales Cycle (No WhatsApp Promotions)
st.title("Cost-Volume-Profit (CVP) Analysis for Smartfoods")

# Inputs for normal sales cycle
st.subheader("Section 1: CVP Analysis for Normal Sales Cycle (No WhatsApp Promotions)")
fixed_costs = st.number_input("Fixed Operating Costs (ZAR)", min_value=0.0)
variable_cost_per_unit = st.number_input("Variable Cost per Basket (Average Variable Cost per Meal, ZAR)", min_value=0.0)
avg_basket_value = st.number_input("Average Basket Value (Average Meal Value, ZAR)", min_value=0.0)
target_profit = st.number_input("Target Profit (Total Profit Goal, ZAR)", min_value=0.0)

# Contribution Margin Calculation
contribution_margin = avg_basket_value - variable_cost_per_unit

if contribution_margin > 0:
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

    # Print breakeven mix and target profit mix
    st.success(f"To break even, you need to sell {break_even_volume:.2f} baskets with total revenue of ZAR {break_even_revenue:,.2f}.")
    st.success(f"To achieve the total profit goal of ZAR {target_profit:,.2f}, you need to sell {target_volume:.2f} baskets with total revenue of ZAR {target_profit_revenue:,.2f}.")

else:
    st.error("Contribution margin is negative. Please adjust input values.")

# Section 2: CVP Analysis Including WhatsApp Promotions
st.subheader("Section 2: CVP Analysis with WhatsApp Promotions")

# Inputs for WhatsApp Promotions (Rearranged order and new placeholders)
whatsapp_messages_sent = st.number_input("Number of WhatsApp Messages Sent", min_value=0)
delivery_rate = st.slider("Delivery Rate (%)", min_value=0.0, max_value=100.0, value=85.0) / 100
conversion_rate = st.slider("Conversion Rate (%)", min_value=0.00, max_value=10.00, value=2.00) / 100

# Input for WhatsApp Cost and Promotional Discount
whatsapp_cost_per_message = st.number_input("Cost per WhatsApp Message (ZAR)", min_value=0.0)
promotional_discount = st.slider("Promotional Discount (%)", min_value=0.0, max_value=100.0, value=10.0) / 100

# WhatsApp Promotion Impact
discounted_basket_value = avg_basket_value * (1 - promotional_discount)
expected_customers = whatsapp_messages_sent * delivery_rate * conversion_rate
st.write(f"Number of converted messages: {expected_customers:.2f}")
expected_sales = expected_customers * discounted_basket_value
total_marketing_cost = whatsapp_messages_sent * whatsapp_cost_per_message

# Calculate the remaining customers needed at regular basket value to reach target profit
remaining_target_profit = target_profit - (expected_customers * discounted_basket_value)
regular_customers_volume = remaining_target_profit / avg_basket_value if remaining_target_profit > 0 else 0

# Total sales volume is regular customers + WhatsApp converted customers
total_sales_volume_corrected = regular_customers_volume + expected_customers
corrected_target_revenue = (regular_customers_volume * avg_basket_value) + (expected_customers * discounted_basket_value)

# Updated break-even volume with WhatsApp promotions
corrected_break_even_volume = (fixed_costs + total_marketing_cost) / contribution_margin

# Display updated results for Section 2
st.success(f"Regular customers (non-discounted): {regular_customers_volume:.2f} customers")
st.success(f"WhatsApp converted customers (discounted): {expected_customers:.2f} customers")
st.success(f"Total sales volume needed: {total_sales_volume_corrected:.2f} customers")
st.success(f"Total revenue to achieve profit goal: ZAR {corrected_target_revenue:,.2f}")
st.success(f"Updated break-even volume: {corrected_break_even_volume:.2f} baskets")

# Graph for Section 2
volumes_with_discount = range(0, int(total_sales_volume_corrected) + 100)
total_costs_with_marketing = [fixed_costs + total_marketing_cost + (variable_cost_per_unit * v) for v in volumes_with_discount]
sales_revenue_with_discount = [avg_basket_value * regular_customers_volume + discounted_basket_value * expected_customers for v in volumes_with_discount]

fig2, ax2 = plt.subplots()
ax2.plot(volumes_with_discount, total_costs_with_marketing, label='Total Costs (Fixed + Variable + Marketing)', color='red')
ax2.plot(volumes_with_discount, sales_revenue_with_discount, label='Sales Revenue', color='green')
ax2.axhline(fixed_costs, color='blue', linestyle='--', label='Fixed + Marketing Costs')

# Plot the updated break-even point
ax2.axvline(corrected_break_even_volume, color='black', linestyle='--', alpha=0.6)
ax2.axhline(corrected_break_even_volume * avg_basket_value, color='black', linestyle='--', alpha=0.6)

# Adjust y-axis in tens of thousands of ZAR
ax2.set_yticklabels([f'{int(tick / 1000):,}k ZAR' for tick in ax2.get_yticks()])

ax2.set_xlabel('Sales Volume (Baskets)')
ax2.set_ylabel('Amount (ZAR)')
ax2.set_title('Cost-Volume-Profit Analysis (With WhatsApp Promotions)')
ax2.legend()

st.pyplot(fig2)


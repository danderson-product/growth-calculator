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


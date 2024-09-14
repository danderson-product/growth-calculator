import streamlit as st
import matplotlib.pyplot as plt

# Section 1: Inputs
st.title("Cost-Volume-Profit (CVP) Analysis with WhatsApp Promotions")

# Input Fields
fixed_costs = st.number_input("Fixed Operating Costs (Monthly)", min_value=0.0)
variable_cost_per_unit = st.number_input("Variable Cost per Basket", min_value=0.0)
avg_basket_value = st.number_input("Average Basket Value", min_value=0.0)
whatsapp_cost_per_message = st.number_input("Cost per WhatsApp Message", min_value=0.0)
delivery_rate = st.slider("Delivery Rate (%)", min_value=0, max_value=100) / 100
conversion_rate = st.slider("Conversion Rate (%)", min_value=0, max_value=100) / 100
promotional_discount = st.slider("Promotional Discount (%)", min_value=0, max_value=100) / 100
target_profit = st.number_input("Target Profit", min_value=0.0)

# Section 2: CVP Calculations
contribution_margin = avg_basket_value * (1 - promotional_discount) - variable_cost_per_unit
if contribution_margin > 0:
    break_even_volume = fixed_costs / contribution_margin
    target_volume = (fixed_costs + target_profit) / contribution_margin
    
    st.write(f"Break-even volume: {break_even_volume:.2f} baskets")
    st.write(f"Volume to achieve target profit: {target_volume:.2f} baskets")
else:
    st.write("Contribution margin is negative. Check input values.")

# Section 3: WhatsApp Campaign Impact
whatsapp_messages_sent = st.number_input("Number of WhatsApp Messages Sent", min_value=0)
expected_customers = whatsapp_messages_sent * delivery_rate * conversion_rate
expected_sales = expected_customers * avg_basket_value * (1 - promotional_discount)

st.write(f"Expected additional customers from WhatsApp promotion: {expected_customers:.2f}")
st.write(f"Expected sales from WhatsApp promotion: ${expected_sales:.2f}")

# Section 4: Updated Break-even with WhatsApp Costs
total_marketing_cost = whatsapp_messages_sent * whatsapp_cost_per_message
updated_fixed_costs = fixed_costs + total_marketing_cost
updated_break_even_volume = updated_fixed_costs / contribution_margin

st.write(f"Updated break-even volume considering WhatsApp costs: {updated_break_even_volume:.2f} baskets")

# Section 5: Visualization
fig, ax = plt.subplots()

# Break-even chart
volumes = range(0, int(target_volume) + 100)
profit_values = [(contribution_margin * v - fixed_costs) for v in volumes]
ax.plot(volumes, profit_values, label='Profit')
ax.axhline(0, color='gray', linestyle='--')
ax.set_xlabel('Sales Volume')
ax.set_ylabel('Profit')
ax.set_title('Cost-Volume-Profit Analysis')
st.pyplot(fig)

# Strategy Design Pattern 

### Input: 

1. current_price
2. day_low
3. day_high

### Abstract Class:

1. condition: core strategy logic 
2. is_order_already_placed_at_this_price: check if any previous order placed for this strategy at this price, use persistent state  
3. on_condition_met: --> when current price meets this strategy, place order 
4. on_condition_not_met: --> when current price does not meets this strategy, just log
5. track_order_placement: --> if on_condition_met, record it in state 

### Execution Flow: 

For the current price,      
    check if condition met  
    check if any order placed for this price from state
    if not 

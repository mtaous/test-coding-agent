#!/usr/bin/env python3
"""
Pumpkin Cake Knowledge Base with Forward, Backward, and Mixed Chaining

This script implements a simple inference engine for reasoning about pumpkin cake preparation
using logical rules and three different chaining strategies.
"""


class PumpkinCakeKnowledgeBase:
    """Knowledge base for pumpkin cake making with inference capabilities."""
    
    def __init__(self):
        """Initialize the knowledge base with facts and rules."""
        # Knowledge Base (Facts)
        self.facts = set([
            'have_pumpkin_puree',
            'have_flour',
            'have_sugar',
            'have_eggs',
            'have_butter',
            'have_baking_powder',
            'have_cinnamon',
            'have_nutmeg',
            'have_mixing_bowl',
            'have_oven',
        ])
        
        # Rule Base (If-Then Rules)
        # Format: {'name': rule_name, 'if': [conditions], 'then': conclusion}
        self.rules = [
            {
                'name': 'wet_ingredients_ready',
                'if': ['have_pumpkin_puree', 'have_eggs', 'have_butter'],
                'then': 'wet_ingredients_prepared'
            },
            {
                'name': 'dry_ingredients_ready',
                'if': ['have_flour', 'have_sugar', 'have_baking_powder'],
                'then': 'dry_ingredients_prepared'
            },
            {
                'name': 'spices_ready',
                'if': ['have_cinnamon', 'have_nutmeg'],
                'then': 'spices_prepared'
            },
            {
                'name': 'batter_ingredients_ready',
                'if': ['wet_ingredients_prepared', 'dry_ingredients_prepared', 'spices_prepared'],
                'then': 'batter_ingredients_complete'
            },
            {
                'name': 'can_mix_batter',
                'if': ['batter_ingredients_complete', 'have_mixing_bowl'],
                'then': 'batter_mixed'
            },
            {
                'name': 'can_bake_cake',
                'if': ['batter_mixed', 'have_oven'],
                'then': 'cake_baking'
            },
            {
                'name': 'cake_done',
                'if': ['cake_baking'],
                'then': 'pumpkin_cake_ready'
            }
        ]
    
    def reset_facts(self, initial_facts=None):
        """Reset facts to initial state or provided facts."""
        if initial_facts:
            self.facts = set(initial_facts)
        else:
            self.facts = set([
                'have_pumpkin_puree',
                'have_flour',
                'have_sugar',
                'have_eggs',
                'have_butter',
                'have_baking_powder',
                'have_cinnamon',
                'have_nutmeg',
                'have_mixing_bowl',
                'have_oven',
            ])
    
    def forward_chaining(self, verbose=True):
        """
        Forward Chaining: Data-driven reasoning.
        Start with known facts and apply rules to derive new facts until no more rules can be applied.
        
        Args:
            verbose: If True, print detailed steps
            
        Returns:
            Set of all derived facts
        """
        if verbose:
            print("\n=== FORWARD CHAINING ===")
            print(f"Initial facts: {sorted(self.facts)}")
        
        derived_facts = self.facts.copy()
        iteration = 0
        
        while True:
            iteration += 1
            new_facts_added = False
            
            if verbose:
                print(f"\nIteration {iteration}:")
            
            for rule in self.rules:
                # Check if all conditions are met
                if all(condition in derived_facts for condition in rule['if']):
                    # Check if conclusion is not already in facts
                    if rule['then'] not in derived_facts:
                        derived_facts.add(rule['then'])
                        new_facts_added = True
                        if verbose:
                            print(f"  Applied rule '{rule['name']}': {rule['if']} → {rule['then']}")
            
            # Stop if no new facts were added
            if not new_facts_added:
                if verbose:
                    print(f"\nNo more rules can be applied.")
                break
        
        if verbose:
            print(f"\nFinal facts: {sorted(derived_facts)}")
            print(f"Total facts derived: {len(derived_facts)}")
        
        return derived_facts
    
    def backward_chaining(self, goal, verbose=True):
        """
        Backward Chaining: Goal-driven reasoning.
        Start with a goal and work backward to see if it can be proved from known facts.
        
        Args:
            goal: The goal fact to prove
            verbose: If True, print detailed steps
            
        Returns:
            Tuple (success: bool, proof_path: list)
        """
        if verbose:
            print("\n=== BACKWARD CHAINING ===")
            print(f"Goal: {goal}")
            print(f"Known facts: {sorted(self.facts)}")
        
        proof_path = []
        visited_goals = set()
        
        def prove_goal(current_goal, depth=0):
            """Recursively try to prove a goal."""
            indent = "  " * depth
            
            # Avoid infinite loops
            if current_goal in visited_goals:
                if verbose:
                    print(f"{indent}Already visited goal: {current_goal}")
                return False
            
            visited_goals.add(current_goal)
            
            # Check if goal is already a known fact
            if current_goal in self.facts:
                if verbose:
                    print(f"{indent}✓ {current_goal} is a known fact")
                proof_path.append(f"{indent}✓ {current_goal} (known fact)")
                return True
            
            # Find rules that conclude this goal
            applicable_rules = [rule for rule in self.rules if rule['then'] == current_goal]
            
            if not applicable_rules:
                if verbose:
                    print(f"{indent}✗ No rules can prove: {current_goal}")
                proof_path.append(f"{indent}✗ {current_goal} (no applicable rules)")
                return False
            
            # Try each applicable rule
            for rule in applicable_rules:
                if verbose:
                    print(f"{indent}Trying rule '{rule['name']}': {rule['if']} → {rule['then']}")
                proof_path.append(f"{indent}Trying rule '{rule['name']}'")
                
                # Try to prove all conditions
                all_conditions_met = True
                for condition in rule['if']:
                    if not prove_goal(condition, depth + 1):
                        all_conditions_met = False
                        break
                
                if all_conditions_met:
                    if verbose:
                        print(f"{indent}✓ Successfully proved {current_goal} using rule '{rule['name']}'")
                    proof_path.append(f"{indent}✓ {current_goal} (proved via rule '{rule['name']}')")
                    return True
            
            # Could not prove goal with any rule
            if verbose:
                print(f"{indent}✗ Failed to prove: {current_goal}")
            proof_path.append(f"{indent}✗ {current_goal} (failed to prove)")
            return False
        
        success = prove_goal(goal)
        
        if verbose:
            print("\n--- Proof Path ---")
            for step in proof_path:
                print(step)
            print(f"\nGoal '{goal}' {'CAN' if success else 'CANNOT'} be proved.")
        
        return success, proof_path
    
    def mixed_chaining(self, goal, verbose=True):
        """
        Mixed Chaining: Combination of forward and backward chaining.
        First use forward chaining to derive what we can, then use backward chaining
        to prove the goal.
        
        Args:
            goal: The goal fact to prove
            verbose: If True, print detailed steps
            
        Returns:
            Tuple (success: bool, forward_facts: set, backward_proof: list)
        """
        if verbose:
            print("\n=== MIXED CHAINING ===")
            print("Step 1: Forward chaining to derive facts...")
        
        # Step 1: Forward chaining
        forward_derived = self.forward_chaining(verbose=verbose)
        
        # Temporarily update facts with forward-derived facts
        original_facts = self.facts.copy()
        self.facts = forward_derived
        
        if verbose:
            print("\nStep 2: Backward chaining to prove goal...")
        
        # Step 2: Backward chaining
        success, proof_path = self.backward_chaining(goal, verbose=verbose)
        
        # Restore original facts
        self.facts = original_facts
        
        if verbose:
            print(f"\n=== MIXED CHAINING RESULT ===")
            print(f"Goal '{goal}' {'CAN' if success else 'CANNOT'} be proved using mixed chaining.")
        
        return success, forward_derived, proof_path


def main():
    """Demonstrate the knowledge base and all three chaining strategies."""
    
    print("=" * 70)
    print("PUMPKIN CAKE KNOWLEDGE BASE - INFERENCE SYSTEM")
    print("=" * 70)
    
    # Initialize knowledge base
    kb = PumpkinCakeKnowledgeBase()
    
    # Demonstrate Forward Chaining
    print("\n" + "=" * 70)
    print("1. FORWARD CHAINING DEMONSTRATION")
    print("=" * 70)
    forward_facts = kb.forward_chaining(verbose=True)
    
    # Demonstrate Backward Chaining
    print("\n" + "=" * 70)
    print("2. BACKWARD CHAINING DEMONSTRATION")
    print("=" * 70)
    goal = 'pumpkin_cake_ready'
    kb.reset_facts()  # Reset to initial facts
    success, proof = kb.backward_chaining(goal, verbose=True)
    
    # Demonstrate Mixed Chaining
    print("\n" + "=" * 70)
    print("3. MIXED CHAINING DEMONSTRATION")
    print("=" * 70)
    kb.reset_facts()  # Reset to initial facts
    success, forward_facts, proof = kb.mixed_chaining('pumpkin_cake_ready', verbose=True)
    
    # Test with incomplete facts
    print("\n" + "=" * 70)
    print("4. TEST WITH INCOMPLETE FACTS")
    print("=" * 70)
    print("Scenario: Missing eggs and butter")
    kb.reset_facts(['have_pumpkin_puree', 'have_flour', 'have_sugar', 
                    'have_baking_powder', 'have_cinnamon', 'have_nutmeg',
                    'have_mixing_bowl', 'have_oven'])
    success, proof = kb.backward_chaining('pumpkin_cake_ready', verbose=True)
    
    print("\n" + "=" * 70)
    print("DEMONSTRATION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()

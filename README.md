# test-coding-agent
Test the Copilot Coding Agent

## Pumpkin Cake Knowledge Base

This repository contains a Python implementation of an inference engine for reasoning about pumpkin cake preparation using logical rules.

### Features

The `pumpkin_cake_knowledge_base.py` script implements:

- **Knowledge Base**: Facts about available ingredients and tools
- **Rule Base**: If-then rules modeling the cake preparation process
- **Forward Chaining**: Data-driven reasoning that derives facts from known information
- **Backward Chaining**: Goal-driven reasoning that proves goals by working backward from conclusions
- **Mixed Chaining**: Hybrid approach combining both forward and backward chaining

### Usage

Run the script to see demonstrations of all three chaining algorithms:

```bash
python3 pumpkin_cake_knowledge_base.py
```

Or make it executable and run directly:

```bash
chmod +x pumpkin_cake_knowledge_base.py
./pumpkin_cake_knowledge_base.py
```

### Example Output

The script demonstrates:
1. Forward chaining deriving all possible facts from initial ingredients
2. Backward chaining proving whether a pumpkin cake can be made
3. Mixed chaining combining both approaches
4. Testing with incomplete facts to show reasoning failures

### Knowledge Representation

**Initial Facts** (ingredients and tools):
- Pumpkin puree, flour, sugar, eggs, butter
- Baking powder, cinnamon, nutmeg
- Mixing bowl, oven

**Rules** (7 inference rules):
1. Wet ingredients preparation
2. Dry ingredients preparation
3. Spices preparation
4. Batter ingredients combination
5. Batter mixing
6. Cake baking
7. Cake completion

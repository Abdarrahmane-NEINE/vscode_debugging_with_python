# VSCode Debugger Cheat Sheet for Python

## Overview
This guide provides a comprehensive overview of using the VSCode debugger for Python development, specifically using the `Payment` class hierarchy as an example. It includes key debugging concepts, practical debugging techniques, and step-by-step instructions to help you efficiently debug Python applications in VSCode.

---

## Setting Up VSCode Debugger
To configure VSCode for debugging Python applications, include the following `launch.json` file in the `.vscode` directory of your project:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Current File",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
}
```

This configuration allows debugging the currently opened Python file in the integrated terminal using VSCode's debugging features.

---

## Debugging Concepts

### Breakpoint
A marker in your code that instructs the debugger to pause execution at a specific line, allowing inspection of variables, the call stack, and execution flow.

### Conditional Breakpoint
A breakpoint that pauses execution only when a specified condition evaluates to true. Useful for debugging specific cases such as invalid credit card numbers.

### Logpoint
A breakpoint alternative that logs messages to the Debug Console instead of pausing execution, enabling non-intrusive debugging.

### Watch Expression (Watch Panel)
A feature that allows monitoring of specific variables or expressions continuously, updating values in real-time during debugging.

### Variables Panel
Displays all variables in the current scope, including local and global variables, along with their current values.

### Call Stack
Shows the sequence of function calls leading to the current execution point, helping to trace the flow and identify potential issues.

### Step Over
Executes the current line of code and moves to the next, without stepping into function calls.

### Step Into
Moves into a function call, allowing line-by-line inspection of its execution.

### Step Out
Executes the remaining lines in the current function and returns to the calling function.

### Debug Console
An interactive interface where you can evaluate expressions, execute code snippets, and view debug logs while debugging.

---

## Debugging Levels

### **Beginner Level**
#### Objective
Learn basic debugging techniques: setting breakpoints, running the debugger, stepping through code, and inspecting variables.

#### Sample Code
```python
import logging

# logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

class Payment:
    def __init__(self, amount: float):
        self.amount = amount

    def process_payment(self) -> bool:
        return False

def main() -> list:
    payment = Payment(100.0)
    result = payment.process_payment()
    return [result]

if __name__ == "__main__":
    final_results = main()
    logging.info("Final Payment Results: %s", final_results)
```

#### Debugging Steps
1. **Set a Breakpoint** on `result = payment.process_payment()`.
2. **Run the Debugger** using `F5`.
3. **Step Over (`F10`)** to see the execution of `process_payment`.
4. **Inspect Variables** in the Variables Panel.

---

### **Intermediate Level**
#### Objective
Understand conditional breakpoints, watch expressions, and navigating multiple functions.

#### Sample Code
```python
class CreditCardPayment(Payment):
    def __init__(self, amount: float, card_number: str, expiry_date: str, cvv: str):
        super().__init__(amount)
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv

    def process_payment(self) -> bool:
        if len(self.card_number) != 16:
            return False
        return True

def main() -> list:
    credit_card_payment = CreditCardPayment(150.0, "1234", "12/24", "123")
    result = credit_card_payment.process_payment()
    return [result]
```

#### Debugging Steps
- **Set a Conditional Breakpoint** on `if len(self.card_number) != 16:`.
- **Run the Debugger** and observe the breakpoint triggering only when `card_number` is invalid.
- **Monitor Values Using Watch Panel** by adding `self.card_number` to track changes.

---

### **Advanced Level**
#### Objective
Master logging, debugging class inheritance, and tracking call stacks.

#### Sample Code
```python
class PayPalPayment(Payment):
    def __init__(self, amount: float, email: str):
        super().__init__(amount)
        self.email = email

    def process_payment(self) -> bool:
        if self.is_email_valid(self.email):
            return False
        return True
    
    def is_email_valid(self, email):
        return "@" in email

def main() -> list:
    paypal_payment = PayPalPayment(75.0, "customerexample.com")
    result = paypal_payment.process_payment()
    return [result]
```

#### Debugging Steps
- **Set a Breakpoint** on `if self.is_email_valid(self.email):` to check email validation logic.
- **Use Logpoints** for non-intrusive debugging:
   ```
   logging.info("Processing PayPal payment for email: %s", self.email)
   ```
- **Inspect the Call Stack** to trace function execution.

---

## Debugging Tools

### Debug Toolbar Shortcuts
- `F5`: Continue execution until the next breakpoint.
- `F10`: Step Over.
- `F11`: Step Into.
- `Shift+F11`: Step Out.

### Panels to Utilize
- **Variables Panel**: Displays variable values.
- **Watch Panel**: Tracks specific expressions.
- **Call Stack Panel**: Shows function execution hierarchy.
- **Debug Console**: Evaluates expressions dynamically.

---

## Best Practices
- Use **Conditional Breakpoints** to filter debugging sessions.
- Implement **Logpoints** for efficient debugging without stopping execution.
- Adjust **launch.json** configurations for various debugging environments.
- Practice debugging techniques to enhance troubleshooting skills.

---

## Conclusion
Mastering VSCode's debugging tools will improve debugging efficiency, streamline development workflows, and enhance problem-solving skills in real-world applications and interviews.


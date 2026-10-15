\# Lab 5: Static Code Analysis — Reflection



\## 1. What is static code analysis, and why is it useful?



Static code analysis examines source code without executing it to identify potential bugs, security vulnerabilities, and style violations. It improves code quality, maintainability, readability, and security.



\## 2. What issues did the tools identify?



Pylint identified missing docstrings, inconsistent naming, a mutable default argument, and other code-quality issues. Bandit identified weak MD5 hashing, a hardcoded password, use of a pseudo-random generator, and shell-command execution risks. Flake8 identified whitespace, blank-line, inline-comment, and line-length violations.



\## 3. How did you address the issues?



I replaced MD5 with SHA-256, used the `secrets` module for bonus-question selection, moved the proctor password to an environment variable, removed the unused remote-lock helper, corrected the mutable default argument, improved function naming and documentation, and fixed formatting issues.



\## 4. What did you learn?



I learned that different static analysis tools detect different categories of issues. Pylint helped improve code quality, Bandit highlighted security risks, and Flake8 enforced consistent formatting. Running the tools again after making changes helped verify the improvements. The final code achieved a Pylint score of 10.00/10, with no reported Bandit issues or Flake8 violations.




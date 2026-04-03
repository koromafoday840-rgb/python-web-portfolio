# 🚀 Backend Mastery Lab
### My Journey to Senior Python Engineer

> "Code is not just about making things work; it's about making things maintainable."

---

## 🗺️ Learning Roadmap (Inspired by roadmap.sh)
- [x] **Phase 1: Python Fundamentals** (Logic, Data Structures)
- [x] **Phase 2: Project Architecture** (Kebab-case naming, Refactoring)
- [/] **Phase 3: Backend Basics** (Flask, API Design)
- [ ] **Phase 4: Database Mastery** (PostgreSQL, SQL Alchemy)

### 🛠 Tech Stack
![Python](https://shields.io)
![Flask](https://shields.io)
![Git](https://shields.io)
![PostgreSQL](https://shields.io)


## 📁 Project Structure
- **/phonebook-manager**: 
  - `manager.py`: Core logic for the contact management system.
  - `README.md`: Documentation explaining the project's mechanical trace and usage.
- **/logic-accumulator**: Core Python logic exercises.
- **/score-tracker**: A functional student performance tracking system.
- **/assets**: Professional documentation and visual demos.
* **/profile-settings:** * `settings.py`: A CRUD-based system for managing user preferences.
    * `README.md`: Documentation covering the logic trace and data-type validation (Boolean/Integer handling).
* `/invoice-consolidation-system`:
    * `invoice-system.py`: Core logic for aggregating sales and merging duplicate items.
    * `README.md`: Technical breakdown of the search-before-insert (upsert) algorithm
    * **/discount-pipeline**:
    * `engine.py`: Core logic for a tiered pricing system.
    * `test_pipeline.py`: Manual execution traces to verify state transitions.
    * **Logic Note**: Implemented a modular data flow where the output of the pricing function is passed as a parameter to the tax validator. This avoids global variables and ensures the "Flow of Truth" is preserved across the stack.
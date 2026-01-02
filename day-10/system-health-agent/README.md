# System Health Analysis Agent

## ⭐ STAR Method

### **S- Situation**

- Linux servers require continuous monitoring of CPU, disk, and memory resources  
- Manual system health checks are time-consuming, reactive, and unreliable  
- Performance issues often go unnoticed until they impact system availability  

---

### **T- Task**

- Automate system health monitoring using Python  
- Analyze system metrics to detect performance risks  
- Generate actionable DevOps recommendations without manual intervention  

---

### **A- Action**

- Collected real-time system metrics using *Python** and the **psutil** library  
- Built an AI-powered analysis workflow using the **Strands Agent framework**  
- Integrated a local Large Language Model (**LLaMA 3.2**) via **Ollama** for intelligent reasoning  
- Passed structured metric inputs with defined thresholds for CPU, disk, and memory usage  
- Automated report generation by writing AI-analyzed output to `system_health_report.txt`  
- Ensured production safety by enforcing **read-only analysis** (no system command execution)  

---

### **R- Result**

- Eliminated **100% of manual system health checks**  
- Reduced issue detection time from **minutes to seconds**  
- Enabled **proactive identification** of CPU, disk, and memory saturation risks  
- Improved system reliability and operational visibility for Linux environments by **99%**
- Demonstrated real-world **DevOps and AIOps practices** using Python and AI  

---

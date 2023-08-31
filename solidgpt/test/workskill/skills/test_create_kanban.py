from solidgpt.src.manager.initializer import Initializer
from solidgpt.src.workgraph.workgraph import *
from solidgpt.src.workagent.agents.agent_principalengineer import AgentPrincipalEngineer
from solidgpt.src.workskill.skills.create_kanban import CreateKanBan

def run_test():
    Initializer()
    app = WorkGraph()
    skill: WorkSkill = CreateKanBan()
    input_path = os.path.join(TEST_DIR, "workskill", "skills", "out", "1", "Write_HLD_Result_1.md")
    skill.init_config(
        [
            {
                "param_path": input_path,
                "loading_method": "SkillInputLoadingMethod.LOAD_FROM_STRING",
                "load_from_output_id": -1
            },
        ],
        [
            {
                "id": 2
            } 
        ])
    agent = AgentPrincipalEngineer(skill)
    node = WorkNode(1, agent)
    app.add_node(node)
    app.init_node_dependencies()
    app.save_data(os.path.join(TEST_DIR, "workskill", "skills", "workspace", "config", "config_data.json"))
    app.execute()

# It is durable work, please run with sudo and give the right access of keyboard.
# example: sudo PYTHONPATH=/Users/wuqiten/Workplace/src-workspace/SolidGPT/ python3 test_skill_usenotion.py
if __name__ == "__main__":
    run_test()

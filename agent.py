import subprocess
from pathlib import Path
from datetime import datetime
import json

def get_git_context(project_path: Path) -> str:
    '''
    Returns data from git history (last commit, recent commits and differences).
    '''
    cmds = {
        "last_commit": ["git", "log", "-1", "--oneline"],
        "recent_commits": ["git", "log", "-3", "--oneline"],
        "diff": ["git", "diff", "--stat"]
    }

    outputs = []

    for name, cmd in cmds.items():
        try:
            out = subprocess.check_output(
                cmd,
                cwd=project_path,
                stderr=subprocess.DEVNULL
            ).decode()
            if out.strip():
                outputs.append(f"{name.upper()}:\n{out}")
        except Exception:
            pass
        
    return "\n".join(outputs)

def get_recent_files(project_path: Path, minutes=120) -> str:
    cutoff = datetime.now().timestamp() - minutes * 60
    recent = []

    for p in project_path.rglob("*"):
        if p.is_file() and p.stat.st_mtime > cutoff:
            recent.append(str(p.relative_to(project_path)))
    
    return recent
        
def build_prompt(project_name, git_ctx, recent_files):
    return f"""
    You are an AI agent helping a developer resume work on a project.

    Project: {project_name}

    Signals of last work:
    {git_ctx}

    Recently edited files:
    {recent_files}

    Generate a concise resume context with:
    1. What the developer was working on
    2. Why (goal / feature / bug)
    3. What the next concrete step should be
    4. A 2-minute re-entry task

    Be specific, avoid generic advice.
    """

def save_context(project_path, context_text):
    store = Path("context_store.json")
    data = json.loads(store.read_text()) if store.exists() else {}
    data[str(project_path)] = {
        "summary": context_text,
        "updated_at": datetime.now().isoformat()
    }
    store.write_text(json.dumps(data, indent=2))

const modules = document.querySelector("#modules");

try {
  const { invoke } = window.__TAURI__.core;
  const descriptors = await invoke("list_modules");
  modules.replaceChildren(...descriptors.map((module) => {
    const card = document.createElement("article");
    const id = document.createElement("code");
    id.textContent = module.id;
    const detail = document.createElement("span");
    detail.textContent = ` · ${module.kind} · API ${module.api_version}`;
    card.append(id, detail);
    return card;
  }));
} catch (error) {
  modules.textContent = `Unable to load modules: ${String(error)}`;
  modules.classList.add("error");
}


import os
from lyzr import Studio

studio = Studio(api_key=os.environ.get("LYZR_API_KEY", "dummy_key"))
agent = studio.create_agent(
    name="hypo-paper-synthesizer",
    provider="openai",
    role="Principal Meta-Science Research Fellow",
    goal="Synthesize scientific literature, extract statistical effect sizes across randomized controlled trials (RCTs), and audit methodologies for replicability risks.",
    instructions="Operate according to OpenGAP specifications."
)

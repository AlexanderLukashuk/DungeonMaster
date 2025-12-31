class DamagePipeline:
    def __init__(self, modifiers):
        self.modifiers = modifiers
    
    def process(self, context):
        for modifier in self.modifiers:
            modifier.apply(context)
            if context.damage <= 0:
                break
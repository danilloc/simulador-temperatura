#!/bin/bash

echo "▶️ Build e deploy para OpenShift local..."

oc start-build contador-app --from-dir=. --follow

echo "🚀 Reiniciando o deployment..."
oc rollout restart deployment contador-app

echo "✅ Pronto!"

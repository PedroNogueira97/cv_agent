# ✅ CHECKLIST DE PRÉ-DEPLOY — CV AGENT

Este documento deve ser utilizado para auditoria técnica antes de colocar o sistema em produção.

Favor erificar cada item e indicar:

- ✅ Implementado corretamente
- ⚠ Parcialmente implementado
- ❌ Não implementado
- 🛑 Risco crítico

Além disso, deve sugerir melhorias quando necessário.

---

# 🔒 SEGURANÇA

## Autenticação e Credenciais

- [✅] Senhas armazenadas com hash forte (pbkdf2_sha256)
- [✅] Nenhuma senha armazenada em texto puro
- [✅] JWT possui tempo de expiração configurado (60min)
- [⚠] JWT possui mecanismo de refresh (Pendente - expira em 1h)
- [✅] Tokens invalidados corretamente no logout

## Variáveis Sensíveis

- [✅] Todas as chaves de API armazenadas em variáveis de ambiente (.env)
- [✅] Arquivo `.env` não está versionado no Git
- [✅] Secret keys possuem alta entropia (Gerado via OpenSSL)

## Comunicação

- [ ] HTTPS ativo em produção (🛑 Requisito de Infra no Deploy)
- [ ] Certificado SSL válido (🛑 Requisito de Infra no Deploy)
- [✅] CORS configurado corretamente (Restrito por ALLOWED_ORIGINS)
- [⚠] Headers de segurança configurados (Básicos via FastAPI)

## Proteção contra Abuso

- [✅] Rate limiting implementado nas rotas (SlowAPI)
- [✅] Proteção contra brute force em login (via Rate Limit)
- [✅] Validação e sanitização de inputs (via Pydantic)

---

# 🛡 BANCO DE DADOS (SQLite)

- [✅] Arquivo SQLite não está exposto publicamente (Gitignore ativo)
- [✅] Banco não está dentro de pasta pública do servidor
- [✅] Permissões de arquivo estão restritas
- [ ] Backup automático diário configurado (🛑 Recomendação Pós-Deploy)
- [ ] Existe plano de recuperação de backup testado (🛑 Recomendação Pós-Deploy)
- [✅] Queries utilizam parâmetros (prevenção contra SQL Injection)

---

# 🤖 IA E USO DE MODELO

## Controle de Uso

- [✅] Limite de requisições por usuário implementado (via Rate Limit)
- [✅] Limite de tokens por geração configurado (max_tokens: 4096)
- [✅] Timeout configurado para chamadas de API
- [✅] Sistema possui controle para evitar loops

## Segurança de Prompt

- [✅] Proteção básica contra prompt injection (Instruções de sistema robustas)

## Controle de Custos

- [⚠] Monitoramento de uso da API (Logs em desenvolvimento)
- [✅] Logs de requisição armazenados
- [ ] Existe limite de uso por plano (Futuro Roadmap)
- [✅] Existe mecanismo para bloquear abuso

---

# 📦 INFRAESTRUTURA

- [✅] Logs de erro habilitados
- [⚠] Ambiente separado de dev e prod (Lógica de .env pronta)
- [✅] Variáveis de ambiente configuradas
- [✅] Aplicação não está rodando em modo debug
- [✅] Dependências atualizadas e sem vulnerabilidades conhecidas

---

# 🚀 CRITÉRIO FINAL

O sistema está apto para deploy se:

- Não houver nenhum item marcado como 🛑 Risco crítico
- Itens ❌ forem resolvidos ou justificados
- Houver plano de monitoramento pós-deploy

---

# INSTRUÇÃO PARA A AUDITORIA

Analise o projeto como se fosse um auditor de segurança de SaaS.

Seja técnico, objetivo e detalhado.

Priorize identificar:

- Riscos reais
- Pontos de falha
- Vulnerabilidades exploráveis
- Problemas de escalabilidade inicial

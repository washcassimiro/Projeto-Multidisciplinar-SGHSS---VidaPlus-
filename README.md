# SGHSS - Sistema de Gestão Hospitalar e de Serviços de Saúde (VidaPlus)
**Projeto Multidisciplinar - UNINTER**

**Aluno:** Washington Cassimiro  
**RU:** 3784294  
**Polo:** Hortolândia - São Paulo  
**Ano:** 2026  

## Sobre o Projeto
O SGHSS visa centralizar a gestão de hospitais e clínicas da rede VidaPlus, integrando cadastros, telemedicina e prontuários com foco em segurança (LGPD) e escalabilidade.

## Tecnologias Propostas (Ênfase Back-end)
- **Banco de Dados:** PostgreSQL
- **Linguagem:** Python
- **Segurança:** Criptografia AES-256 e logs de auditoria imutáveis.

## Funcionalidades Principais
- Cadastro de Pacientes e Profissionais.
- Agendamento de Consultas (Presenciais/Telemedicina).
- Gestão de Prontuários e Leitos Hospitalares.

classDiagram
    class Paciente {
        +int id
        +string nome
        +string cpf
        +date data_nasc
        +int historico_id (FK)
    }
    class Profissional {
        +int id
        +string nome
        +string crm_coren
        +string especialidade
    }
    class Consulta {
        +int id
        +int paciente_id (FK)
        +int profissional_id (FK)
        +datetime data_hora
        +string tipo (presencial/telemedicina)
    }
    class Prontuario {
        +int id
        +int paciente_id (FK)
        +string descricao
        +datetime data_registro
        +string logs_auditoria
    }

    Paciente "1" -- "*" Consulta : realiza
    Profissional "1" -- "*" Consulta : atende
    Paciente "1" -- "1" Prontuario : possui

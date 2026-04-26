from datetime import datetime

# Exemplo de lógica para o agendamento de consultas (RF02)
def agendar_consulta(paciente_id, prof_id, horario):
    if verificar_disponibilidade(prof_id, horario):
        # Lógica para salvar no banco de dados
        confirmar_agendamento(paciente_id, prof_id, horario)
        return "Consulta confirmada com sucesso!"
    else:
        return "Erro: Horário já ocupado."

  # RF05 - Controle de acesso por perfil (Segurança)
def acessar_prontuario(usuario_id, paciente_id):
    usuario = buscar_usuario_no_banco(usuario_id)
    
    # Somente perfis 'MEDICO' podem visualizar prontuários detalhados
    if usuario.perfil == "MEDICO":
        prontuario = buscar_prontuario(paciente_id)
        registrar_log_auditoria(usuario_id, f"Acessou prontuário do paciente {paciente_id}") # 
        return prontuario
    else:
        registrar_log_auditoria(usuario_id, "Tentativa de acesso negada")
        return "Erro: Acesso negado. Perfil insuficiente."

  # RF03 - Atualizar prontuário e emitir receitas digitais
def atualizar_prontuario(profissional_id, paciente_id, novas_notas, receita_digital):
    # Simula a atualização no banco de dados
    prontuario = buscar_prontuario(paciente_id)
    prontuario.descricao += f"\n Nova entrada: {novas_notas}"
    prontuario.receita = receita_digital
    
    # Registro de log obrigatório para compliance 
    log = f"Alteração por Profissional {profissional_id} em {datetime.now()}"
    prontuario.logs_auditoria += f" | {log}"
    
    salvar_no_banco(prontuario)
    return "Prontuário e receita atualizados com sucesso."

package br.ce.wcaquino.steps;

import br.ce.wcaquino.entidades.Filme;
import br.ce.wcaquino.entidades.NotaAluguel;
import br.ce.wcaquino.servicos.AluguelService;

public class AlugarFilmeStepsData {
	private Filme filme;
	private AluguelService aluguel;
	private NotaAluguel nota;
	private String erro;
	private String tipoAluguel;

	public AlugarFilmeStepsData(AluguelService aluguel) {
		this.aluguel = aluguel;
	}

	public Filme getFilme() {
		return filme;
	}

	public void setFilme(Filme filme) {
		this.filme = filme;
	}

	public AluguelService getAluguel() {
		return aluguel;
	}

	public void setAluguel(AluguelService aluguel) {
		this.aluguel = aluguel;
	}

	public NotaAluguel getNota() {
		return nota;
	}

	public void setNota(NotaAluguel nota) {
		this.nota = nota;
	}

	public String getErro() {
		return erro;
	}

	public void setErro(String erro) {
		this.erro = erro;
	}

	public String getTipoAluguel() {
		return tipoAluguel;
	}

	public void setTipoAluguel(String tipoAluguel) {
		this.tipoAluguel = tipoAluguel;
	}
}
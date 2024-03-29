package br.ce.wcaquino.steps;

import java.io.File;
import java.io.IOException;

import org.apache.commons.io.FileUtils;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

import cucumber.api.Scenario;
import cucumber.api.java.After;
import cucumber.api.java.Before;
import cucumber.api.java.pt.Dado;
import cucumber.api.java.pt.Entao;
import cucumber.api.java.pt.Quando;

public class InserirContasSteps {

	private WebDriver driver;

	@Dado("^que desejo adicionar uma conta$")
	public void queDesejoAdicionarUmaConta() throws Throwable {
		System.setProperty("webdriver.gecko.driver",
				"C:\\Users\\Pedro\\Desktop\\Carolina\\geckoDriver\\geckodriver.exe");
		driver = new FirefoxDriver();
		driver.get("http://srbarriga.herokuapp.com");
		driver.findElement(By.id("email")).sendKeys("carol@carol");
		driver.findElement(By.id("senha")).sendKeys("aaa");
		driver.findElement(By.tagName("button")).click();
		driver.findElement(By.linkText("Contas")).click();
		driver.findElement(By.linkText("Adicionar")).click();

	}

	@Quando("^adiciono a  conta \"([^\"]*)\"$")
	public void adicionoAConta(String arg1) throws Throwable {
		driver.findElement(By.id("nome")).sendKeys(arg1);
		driver.findElement(By.tagName("button")).click();

	}

	@Entao("^recebo a mensagem \"([^\"]*)\"$")
	public void receboAMensagem(String arg1) throws Throwable {
		String texto = driver.findElement(By.xpath("//div[(@class, 'alert alert-')]")).getText();
		Assert.assertEquals(arg1, texto);
	}

	@Before(order = 0)
	public void inicio() {
		System.out.println("COMECANDO AQUI");
	}

	@Before(order = 1)
	public void inicio2() {
		System.out.println("COMECANDO AQUI ,PARTE 2");
	}

	@After(order = 1, value = { "~@funcionais" })
	public void screenshot(Scenario cenario) {
		File file = ((TakesScreenshot) driver).getScreenshotAs(OutputType.FILE);
		try {
			FileUtils.copyFile(file, new File("target/screenshots/" + cenario.getId() + ".jpg"));
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	@After(order = 0, value = { "~@funcionais" })
	public void fecharBrowser() {
		driver.quit();
		System.out.println("TERMINANDO");

	}

}

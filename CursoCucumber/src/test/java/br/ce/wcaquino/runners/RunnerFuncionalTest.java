package br.ce.wcaquino.runners;
import org.junit.BeforeClass;
import org.junit.runner.RunWith;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

import cucumber.api.CucumberOptions;
import cucumber.api.SnippetType;
import cucumber.api.junit.Cucumber;

@RunWith(Cucumber.class)
@CucumberOptions(
		features="src/test/resources/feature/",
		glue="br.ce.wcaquino.steps",
		tags= {"@funcionais","~@ignore"},
		plugin = {"pretty","html:target/report-html","json:target/report.json"},
		monochrome = true,
		snippets = SnippetType.CAMELCASE,
		dryRun = false,	
		strict = false
		)
public class RunnerFuncionalTest {
	
	@BeforeClass
	public static void reset() {
		System.setProperty("webdriver.gecko.driver",
				"C:\\Users\\Pedro\\Desktop\\Carolina\\geckoDriver\\geckodriver.exe");
		WebDriver driver = new FirefoxDriver();
		driver.get("http://srbarriga.herokuapp.com");
		driver.findElement(By.id("email")).sendKeys("carol@carol");
		driver.findElement(By.name("senha")).sendKeys("aaa");
		driver.findElement(By.tagName("button")).click();
		driver.findElement(By.linkText("reset")).click();
		driver.quit();
		
	}
	

}

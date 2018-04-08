import java.util.ArrayList;
import java.util.List;

public class Enemy extends Character {

	public Enemy(String name, int hitPoints, Weapon weapon) {
		super(name, hitPoints, weapon);
	}

	/**
	 * Create multiple copies of an enemy
	 * @param enemyToCopy
	 * @param numberOfCopies
	 * @return List of enemies to copy
	 */
	public List<Enemy> copy(Enemy enemyToCopy, int numberOfCopies) {
		List<Enemy> enemies = new ArrayList<Enemy>();
		for(int i=0; i<numberOfCopies; i++) {
			Weapon copyWeapon = new Weapon(enemyToCopy.getWeapon().getName(), enemyToCopy.getWeapon().getNumberOfDice(),
					enemyToCopy.getWeapon().getNumberOfSidesPerDie(), enemyToCopy.getWeapon().getDamageType());
			Enemy newEnemy = new Enemy(enemyToCopy.getName(), enemyToCopy.getHitPoints(), copyWeapon);
			newEnemy.setResistances(enemyToCopy.getResistances());
			newEnemy.setVulnerabilities(enemyToCopy.getVulnerabilities());
			enemies.add(newEnemy);
		}
		return enemies;
	}
}
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Character {

	private String name;
	private int hitPoints;
	private Weapon weapon;
	private List<DamageType> vulnerabilities;
	private List<DamageType> resistances;
	
	public Character(String name, int hitPoints, Weapon weapon)
	{
		setName(name);
		setHitPoints(hitPoints);
		setWeapon(weapon);
		vulnerabilities = new ArrayList<>();
		resistances = new ArrayList<>();
	}

	/**
	 * @return the name
	 */
	public String getName() {
		return name;
	}

	/**
	 * @param name the name to set
	 */
	public void setName(String name) {
		this.name = name;
	}

	/**
	 * @return the hitPoints
	 */
	public int getHitPoints() {
		return hitPoints;
	}

	/**
	 * @param hitPoints the hitPoints to set
	 */
	public void setHitPoints(int hitPoints) {
		this.hitPoints = hitPoints;
	}

	/**
	 * @return the weapon
	 */
	public Weapon getWeapon() {
		return weapon;
	}

	/**
	 * @param weapon the weapon to set
	 */
	public void setWeapon(Weapon weapon) {
		this.weapon = weapon;
	}
	
	public void addResistance(DamageType damageType) {
		resistances.add(damageType);
	}
	public void removeResistance(DamageType damageType) {
		resistances.remove(damageType);
	}
	public void addVulnerability(DamageType damageType) {
		vulnerabilities.add(damageType);
	}
	public void removeVulnerability(DamageType damageType) {
		vulnerabilities.remove(damageType);
	}
	public boolean isResistant(DamageType damageType) {
		return resistances.contains(damageType);
	}
	public boolean isVulnerable(DamageType damageType) {
		return vulnerabilities.contains(damageType);
	}
	
	/**
	 * @return the vulnerabilities
	 */
	public List<DamageType> getVulnerabilities() {
		return vulnerabilities;
	}

	/**
	 * @param vulnerabilities the vulnerabilities to set
	 */
	public void setVulnerabilities(List<DamageType> vulnerabilities) {
		this.vulnerabilities = vulnerabilities;
	}

	/**
	 * @return the resistances
	 */
	public List<DamageType> getResistances() {
		return resistances;
	}

	/**
	 * @param resistances the resistances to set
	 */
	public void setResistances(List<DamageType> resistances) {
		this.resistances = resistances;
	}

	public boolean isDead() {
		return hitPoints < 0;
	}
	public int attack(Character target) {
		int damage = 0;
		for(int i=0; i<getWeapon().getNumberOfDice(); i++)
		{
			Random random = new Random();
	        damage  += random.nextInt(getWeapon().getNumberOfSidesPerDie()) + 1; 
		}
		if(target.isResistant(getWeapon().getDamageType())) {
			damage = (int) (damage*0.5);
		} else if(target.isVulnerable(getWeapon().getDamageType())) {
			System.out.println(target.getName()+" is vulnerable!");
			damage = (int) (damage*1.5);
		}
		target.setHitPoints(target.getHitPoints()-damage);
		return damage;
	}
}

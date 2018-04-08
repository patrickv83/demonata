
public class Weapon extends Item {

	private int numberOfDice;
	private int numberOfSidesPerDie;
	private DamageType damageType;
	
	Weapon(String name, int numberOfDice, int numberOfSidesPerDie, DamageType damageType) {
		super(name);
		setNumberOfDice(numberOfDice);
		setNumberOfSidesPerDie(numberOfSidesPerDie);
		setDamageType(damageType);
	}

	/**
	 * @return the numberOfDice
	 */
	public int getNumberOfDice() {
		return numberOfDice;
	}

	/**
	 * @param numberOfDice the numberOfDice to set
	 */
	public void setNumberOfDice(int numberOfDice) {
		this.numberOfDice = numberOfDice;
	}

	/**
	 * @return the numberOfSidesPerDie
	 */
	public int getNumberOfSidesPerDie() {
		return numberOfSidesPerDie;
	}

	/**
	 * @param numberOfSidesPerDie the numberOfSidesPerDie to set
	 */
	public void setNumberOfSidesPerDie(int numberOfSidesPerDie) {
		this.numberOfSidesPerDie = numberOfSidesPerDie;
	}

	/**
	 * @return the damageType
	 */
	public DamageType getDamageType() {
		return damageType;
	}

	/**
	 * @param damageType the damageType to set
	 */
	public void setDamageType(DamageType damageType) {
		this.damageType = damageType;
	}
	
}
